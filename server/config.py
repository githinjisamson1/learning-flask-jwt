from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from os import environ


app = Flask(__name__)
load_dotenv()

app.secret_key = environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = environ.get(
    "SQLALCHEMY_TRACK_MODIFICATIONS")
app.json.compact = False

db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)
