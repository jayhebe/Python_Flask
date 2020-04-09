from application import app
from controllers.index import index_page


app.register_blueprint(index_page, url_prefix="/")
