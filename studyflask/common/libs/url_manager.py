from application import app
from common.libs.date_time_helper import get_current_time


class UrlManager:
    @staticmethod
    def build_url(path):
        config_domain = app.config["DOMAIN"]
        return "{}{}".format(config_domain["www"], path)

    @staticmethod
    def build_static_url(path):
        path = "/static" + path + "?ver=" + UrlManager.get_release_version()
        return UrlManager.build_url(path)

    @staticmethod
    def get_release_version():
        ver = "{}".format(get_current_time("%Y%m%d%H%M%S"))
        release_version = app.config.get("RELEASE_VERSION")
        return release_version if release_version else ver
