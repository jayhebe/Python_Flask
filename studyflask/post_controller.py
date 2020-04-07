from flask import Blueprint


post_page = Blueprint("post_page", __name__)


@post_page.route("/index/")
def post_index():
    return "Post index"


@post_page.route("/info/")
def post_info():
    return "Post info"


@post_page.route("/set/")
def post_set():
    return "Post modify"


@post_page.route("/ops/")
def post_ops():
    return "Post operations"
