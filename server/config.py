from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from os import environ
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


# !contains basic configurations
app = Flask(__name__)
db = SQLAlchemy()
load_dotenv()

app.secret_key = environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = environ.get(
    "SQLALCHEMY_TRACK_MODIFICATIONS")
app.config["SQLALCHEMY_ECHO"] = environ.get("SQLALCHEMY_ECHO")
app.config["JWT_SECRET_KEY"] = environ.get("JWT_SECRET_KEY")
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
# JWTManager().init_app(app)

# !resolve circular import error
# ensure db = SQLAlchemy is initialized here
