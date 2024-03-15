from flask import Flask, render_template, request
from cloudinary import CloudinaryUploader, config
from dotenv import load_dotenv
from os import environ

load_dotenv()

app = Flask(__name__)

# Configure Cloudinary
config(
    cloud_name=environ.get("CLOUD_NAME"),
    api_key=environ.get("API_KEY"),
    api_secret=environ.get("API_SECRET")
)
