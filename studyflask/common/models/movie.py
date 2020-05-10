from application import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    actors = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    cover_pic = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue())
    pics = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())
    url = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue())
    description = db.Column(db.Text, server_default=db.FetchedValue())
    magnet_url = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue())
    hash_value = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    pub_date = db.Column(db.DateTime, server_default=db.FetchedValue())
    source = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue())
    view_counter = db.Column(db.Integer, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
