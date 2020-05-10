from application import app
from flask import request, g

from common.models.user import User
from common.models.movie import Movie
from common.libs.user_service import UserService


@app.before_request
def before_request():
    app.logger.info("---------------before request---------------")
    user_info = check_login()
    g.current_user = None
    g.movie_info = None
    if user_info:
        movie_info = Movie.query.all()

        g.current_user = user_info
        g.movie_info = movie_info

    return


@app.after_request
def after_request(response):
    app.logger.info("---------------after request---------------")
    return response


def check_login():
    cookies = request.cookies
    auth_cookies = cookies["auth_cookie"] if "auth_cookie" in cookies else ""

    if auth_cookies is None:
        return False

    auth_info = auth_cookies.split("#")
    if len(auth_info) != 2:
        return False

    try:
        user_info = User.query.filter_by(id=auth_info[1]).first()
        movie_info = Movie.query.all()
    except Exception:
        return False

    if user_info is None:
        return False

    if auth_info[0] != UserService.generate_auth_code(user_info):
        return False

    return user_info
