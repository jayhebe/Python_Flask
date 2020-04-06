from flask import Flask
from post_controller import post_page

app = Flask(__name__)
app.config.from_pyfile("config/base_settings.py")

app.register_blueprint(post_page, url_prefix="/post")


if __name__ == "__main__":
    app.run()
