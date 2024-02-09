from flask import Flask


# create application factory
def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()

    return app
