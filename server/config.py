from flask import Flask
from flask_migrate import Migrate
from models import db
from dotenv import load_dotenv
from os import environ
from flask.ext.bcrypt import Bcrypt

# contains basic configurations
app = Flask(__name__)
load_dotenv()

app.secret_key = environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = environ.get(
    "SQLALCHEMY_TRACK_MODIFICATIONS")
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)
