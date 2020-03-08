from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug import secure_filename
from .tools.extract import read_head, read_content

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
            for excel_header in excel_headers.items():
                flash(excel_header)
            return redirect(url_for("index", filename=file_name))

    return render_template("index.html")


@app.route('/list_content', methods=["GET", "POST"])
def list_content():
    if request.method == "POST":
        excel_headers = request.form.getlist("excel_headers")
        excel_headers = [int(col) for col in excel_headers]
        excel_filename = request.form.get("filename")
        excel_filepath = os.path.join(app.config["UPLOAD_FOLDER"], excel_filename)
        excel_result = read_content(excel_filepath, excel_headers)

        flash(excel_result)

    return render_template("list.html")
