from flask import Flask, request


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
