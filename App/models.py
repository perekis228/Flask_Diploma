from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    author = db.Column(db.String(30))
    genre = db.Column(db.String(30))
    description = db.Column(db.String(30))