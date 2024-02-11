from flask import Blueprint
from flask_restful import Api, Resource

auth_bp = Blueprint("auth_bp", __name__)
api = Api(auth_bp)


class Register(Resource):
    def post(self):
        pass


api.add_resource(Register, "/register")
