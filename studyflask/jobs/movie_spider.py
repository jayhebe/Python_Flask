from bs4 import BeautifulSoup
from flask_script import Command
import requests
import hashlib

from common.models.movie import Movie
from common.libs.date_time_helper import get_current_time
from application import db, app


movie_base_url = "http://btbtdy1.com"
movie_download_base_url = "http://btbtdy1.com/vidlist/"
movie_page_url = "http://btbtdy1.com/btfl/dy1-{}.html"
movie_page_range = 1
movie_headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/71.0.3578.98 Safari/537.36'
}


def get_page_info():
    page_info_list = []
    for page in range(movie_page_range):
        page_res = requests.get(movie_page_url.format(page + 1), headers=movie_headers)
        page_res.encoding = page_res.apparent_encoding
        if page_res.status_code != 200:
            return None

        page_bs = BeautifulSoup(page_res.text, "html.parser")
        page_info = page_bs.find_all("div", class_="liimg")

        for info in page_info:
            page_info_list.append(info)

        return page_info_list


def get_movie_link(page_info_list):
    movie_link_list = []
    for page_info in page_info_list:
        movie_link = movie_base_url + page_info.find("a")["href"]

        movie_link_list.append(movie_link)

    return movie_link_list


def parse_movie_info(movie_link_list):
    movie_info_list = []
    for movie_link in movie_link_list:
        movie_info = dict()

        movie_res = requests.get(movie_link, headers=movie_headers)
        movie_res.encoding = movie_res.apparent_encoding
        if movie_res.status_code != 200:
            return None

        movie_bs = BeautifulSoup(movie_res.text, "html.parser")

        movie_info["链接"] = movie_link

        movie_intro = movie_bs.find("div", class_="vod_intro rt")

        movie_name = movie_intro.find("h1").text.strip()
        movie_info["电影名"] = movie_name

        movie_meta_key = movie_intro.find_all("dt")
        movie_meta_value = movie_intro.find_all("dd")
        for meta_key, meta_value in zip(movie_meta_key, movie_meta_value):
            movie_info[meta_key.text.replace(":", "")] = meta_value.text.replace("\xa0", " ").strip()

        movie_description = movie_intro.find("div", class_="c05").text.replace('"', "").strip()
        movie_info["剧情介绍"] = movie_description

        movie_cover = movie_bs.find("div", class_="vod_img lf").find("img")["src"]
        movie_info["封面图"] = movie_cover

        movie_download_list = []
        movie_download_page = movie_download_base_url + movie_link[movie_link.rindex("/") + 3:]
        movie_download_res = requests.get(movie_download_page, headers=movie_headers)
        movie_download_res.encoding = movie_download_res.apparent_encoding
        if movie_download_res.status_code == 200:
            movie_download_bs = BeautifulSoup(movie_download_res.text, "html.parser")
            movie_download_links = movie_download_bs.find_all("a", class_="d1")
            for movie_download_link in movie_download_links:
                movie_download_list.append(movie_download_link["href"])

            movie_info["下载链接"] = movie_download_list

        movie_info_list.append(movie_info)

    return movie_info_list


def write_database(movie_info_list):
    for movie_info in movie_info_list:
        model_movie = Movie()
        model_movie.name = movie_info["电影名"]
        model_movie.classify = movie_info["类型"]
        model_movie.actors = movie_info["主演"]
        model_movie.cover_pic = movie_info["封面图"]
        model_movie.pics = movie_info["封面图"]
        model_movie.url = movie_info["链接"]
        model_movie.description = movie_info["剧情介绍"]
        model_movie.magnet_url = ", ".join(movie_info["下载链接"])
        hash_value = hashlib.md5(movie_info["链接"].encode("utf-8")).hexdigest()
        model_movie.hash_value = hash_value
        model_movie.pub_date = get_current_time()
        model_movie.source = movie_info["链接"]
        model_movie.created_time = get_current_time()
        model_movie.updated_time = get_current_time()

        is_exist_hash_value = Movie.query.filter_by(hash_value=hash_value).first()
        if is_exist_hash_value:
            continue

        db.session.add(model_movie)
        db.session.commit()


class MovieSpider(Command):

    help = description = "Runs the spider to grab movie information"

    def run(self):
        app.logger.info("Starting spider")

        list_page_info = get_page_info()
        list_movie_link = get_movie_link(list_page_info)
        list_movie_info = parse_movie_info(list_movie_link)
        write_database(list_movie_info)
