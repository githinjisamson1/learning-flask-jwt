from flask import Blueprint
from flask_restful import Api, Resource

user_bp = Blueprint("user_bp", __name__)
api = Api(user_bp)


class Index(Resource):
    def get(self):
        return {"success": True, "message": "Hello World"}


api.add_resource(Index, "/")
