from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile("config/base_settings.py")
app.config["SQLALCHEMY_DATABASE_URI"] = ""
db = SQLAlchemy(app)
