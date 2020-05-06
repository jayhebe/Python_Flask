from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

import os


app = Flask(__name__)

app.config.from_pyfile("config/base_settings.py")

# ops_config=local|production
# Linux: export ops_config=local|production
# Windows: set ops_config=local|production
if "ops_config" in os.environ:
    app.config.from_pyfile("config/{}_settings.py".format(os.environ["ops_config"]))

db = SQLAlchemy(app)

manager = Manager(app)
