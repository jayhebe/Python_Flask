from flask import Blueprint, request, make_response, jsonify, render_template
from common.models.books import Book
# from sqlalchemy import text
# from application import db

import json

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index():
    return "I love Flask"


@index_page.route("/get")
def get():
    var_a = request.args.get("a", "flask")
    return "request: %s, params: %s, var_a: %s" % (request.method, request.args, var_a)


@index_page.route("/post", methods=["POST"])
def post():
    var_a = request.form["a"] if "a" in request.form else ""
    return "request: %s, params: %s, var_a: %s" % (request.method, request.form, var_a)


@index_page.route("/both", methods=["GET", "POST"])
def both():
    value = request.values["a"] if "a" in request.values else "default value"
    return "request: %s, params: %s, value: %s" % (request.method, request.form, value)


@index_page.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    return "request: %s, params: %s, file: %s" % (request.method, request.files, f)


@index_page.route("/text_same")
def text_same():
    response = make_response("text/html", 200)
    return response


@index_page.route("/json")
def my_json():
    data = {"a": "b"}
    response = make_response(json.dumps(data))
    response.headers["Content-Type"] = "application/json"
    return response


@index_page.route("/json_same")
def json_same():
    data = {"a": "b"}
    response = make_response(jsonify(data))
    return response


@index_page.route("/template")
def template():
    context = dict()
    context["user"] = {
        "name": "Jay",
        "nickname": "Jayhebe",
        "qq": "330329721",
        "home_page": "http://www.myclouodway.cn"
    }
    context["num_list"] = [1, 2, 3, 4, 5]

    return render_template("index.html", **context)


@index_page.route("/search")
def search():
    context = dict()
    # sql = text("select * from book")
    # result = db.engine.execute(sql)

    result = Book.query.all()
    context["result"] = result

    return render_template("index.html", **context)
