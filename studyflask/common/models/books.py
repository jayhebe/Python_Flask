from application import db


class Book(db.Model):
    bid = db.Column(db.Integer(), primary_key=True)
    bname = db.Column(db.String(20))
    price = db.Column(db.Float())
    btypeid = db.Column(db.Integer())
