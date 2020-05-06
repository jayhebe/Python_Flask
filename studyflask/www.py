from interceptors.auth import *
from interceptors.error_handler import *
from common.libs.url_manager import UrlManager

from controllers.index import index_page
from controllers.member import member_page
from application import app


app.register_blueprint(index_page, url_prefix="/")
app.register_blueprint(member_page, url_prefix="/member")

app.add_template_global(UrlManager.build_url, "build_url")
app.add_template_global(UrlManager.build_static_url, "build_static_url")
