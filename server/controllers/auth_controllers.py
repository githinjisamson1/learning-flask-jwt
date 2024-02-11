from flask import Blueprint, make_response, jsonify
from flask_restful import Api, Resource, reqparse
from config import db, bcrypt
from models import User

auth_bp = Blueprint("auth_bp", __name__)
api = Api(auth_bp)

# user data
parser = reqparse.RequestParser()
parser.add_argument('username', required=True, help="Username required")
parser.add_argument('email', required=True, help="Email required")
parser.add_argument('password', required=True, help="Password required")


# auth resources
class Register(Resource):
    def post(self):
        args = parser.parse_args()

        new_user = User(
            username=args["username"],
            email=args["email"],
            _password_hash=bcrypt.generate_password_hash(
                args["password"].encode('utf-8'))
        )

        db.session.add(new_user)
        db.session.commit()

        return make_response(jsonify(new_user.to_dict()), 201)


api.add_resource(Register, "/register")
