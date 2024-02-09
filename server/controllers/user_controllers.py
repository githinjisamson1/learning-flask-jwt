from flask import Blueprint, make_response, jsonify
from flask_restful import Api, Resource, reqparse
from models import db, User

parser = reqparse.RequestParser()
parser.add_argument('username', required=True, help="Username required")
parser.add_argument('email', required=True, help="Email required")
parser.add_argument('password', required=True, help="Password required")
# args = parser.parse_args()

user_bp = Blueprint("user_bp", __name__)
api = Api(user_bp)


class Index(Resource):
    def get(self):
        return {"success": True, "message": "Hello World"}


class Register(Resource):
    def post(self):
        args = parser.parse_args()
        new_user = User(
            username=args["username"],
            email=args["email"],
            password=args["password"]
        )

        db.session.add(new_user)
        db.session.commit()

        return make_response(jsonify(new_user.to_dict()), 201)


api.add_resource(Index, "/")
api.add_resource(Register, "/users")
