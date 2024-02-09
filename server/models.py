from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from config import bcrypt

# from uuid import uuid4

db = SQLAlchemy()


# wil contain models
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    # columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    

    # validate username
    @validates("username")
    def validate_username(self, key, username):
        if not username:
            raise ValueError("Username required")
        else:
            if username in [user.username for user in User.query.all()]:
                raise ValueError("Username already exists")
            return username

    # validate email
    @validates("email")
    def validate_email(self, key, email):
        if not email:
            raise ValueError("Email required")
        
        else:
            if email in [user.email for user in User.query.all()]:
                raise ValueError("Email already exists")
            
            else:
                import re
                pattern = r"[a-z0-9]*@gmail.com"
                regex = re.compile(pattern)

                if not regex.fullmatch(email):
                    raise ValueError("Invalid email format")
                
                return email

    def __repr__(self):
        return f"User {self.username} {self.email}"
