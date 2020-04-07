from flask import Flask, request, make_response, jsonify, render_template
import json

app = Flask(__name__)
# app.config.from_object("config.base_settings")
app.config.from_pyfile("config/base_settings.py")


@app.route("/")
def index():
    return "I love Flask"


@app.route("/get")
def get():
    var_a = request.args.get("a", "flask")
    return "request: %s, params: %s, var_a: %s" % (request.method, request.args, var_a)


@app.route("/post", methods=["POST"])
def post():
    var_a = request.form["a"] if "a" in request.form else ""
    return "request: %s, params: %s, var_a: %s" % (request.method, request.form, var_a)


@app.route("/both", methods=["GET", "POST"])
def both():
    value = request.values["a"] if "a" in request.values else "default value"
    return "request: %s, params: %s, value: %s" % (request.method, request.form, value)


@app.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    return "request: %s, params: %s, file: %s" % (request.method, request.files, f)


@app.route("/text")
def text():
    return "text/html"


@app.route("/text_same")
def text_same():
    response = make_response("text/html", 200)
    return response


@app.route("/json")
def my_json():
    data = {"a": "b"}
    response = make_response(json.dumps(data))
    response.headers["Content-Type"] = "application/json"
    return response


@app.route("/json_same")
def json_same():
    data = {"a": "b"}
    response = make_response(jsonify(data))
    return response


@app.route("/template")
def template():
    return render_template("index.html")

#
#
# @app.route("/my/")
# def my():
#     return "my page"
#
#
# @app.route("/my/<username>/")
# def user(username):
#     return "Hello, %s" % username


if __name__ == "__main__":
    app.run(host="0.0.0.0")
