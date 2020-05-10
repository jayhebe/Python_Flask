from flask import Blueprint

from common.libs.helper import render_page

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index():
    return render_page("index.html")
