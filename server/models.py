from config import db
from uuid import uuid4


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, default=str(uuid4()))
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"User {self.username} {self.email}"
