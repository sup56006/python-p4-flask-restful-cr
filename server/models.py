from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Newsletter(db.Model, SerializerMixin):
    __tablename__ = 'newsletters'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    published_at = db.Column(db.DateTime)
    edited_at = db.Column(db.DateTime)
