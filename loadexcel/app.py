from flask import Flask, render_template, request
from werkzeug import secure_filename
from tools.extract import read_head, read_content

import os


app = Flask(__name__)
app.config["SECRET_KEY"] = "excel demo key"
app.config['UPLOAD_FOLDER'] = os.getcwd() + os.path.sep + "files"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        excel_file = request.files["file"]
        if excel_file:
            file_name = secure_filename(excel_file.filename)
            excel_file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))
            excel_headers = read_head(os.path.join(app.config["UPLOAD_FOLDER"], file_name))

            excel_result = dict()
            excel_result["file_name"] = file_name
            excel_result["excel_headers"] = excel_headers

            return render_template("index.html", **excel_result)

    return render_template("index.html")


@app.route('/list_content', methods=["GET", "POST"])
def list_content():
    if request.method == "POST":
        excel_headers = request.form.getlist("excel_headers")
        excel_headers = [int(col) for col in excel_headers]
        excel_filename = request.form.get("filename")
        excel_filepath = os.path.join(app.config["UPLOAD_FOLDER"], excel_filename)
        excel_result = read_content(excel_filepath, excel_headers)

        list_result = dict()
        list_result["excel_result"] = excel_result

        return render_template("list.html", **list_result)

    return render_template("list.html")
