from application import app
from index_controller import index_page


app.register_blueprint(index_page, url_prefix="/studyflask")
