from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
# from uuid import uuid4

db = SQLAlchemy()


# wil contain models
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"User {self.username} {self.email}"
