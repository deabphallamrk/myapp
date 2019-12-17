from app import db

class TBL_POST(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(35))
    content = db.Column(db.String(250))