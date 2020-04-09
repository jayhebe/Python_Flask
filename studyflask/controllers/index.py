from flask import Blueprint, request, make_response, jsonify, render_template
from common.models.books import Book

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index():
    context = dict()

    result = Book.query.all()
    context["result"] = result

    return render_template("index.html", **context)
