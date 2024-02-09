from flask import Blueprint, make_response, jsonify, request
from flask_restful import Api, Resource, reqparse
from models import db, User

parser = reqparse.RequestParser()
parser.add_argument('username', required=True, help="Username required")
parser.add_argument('email', required=True, help="Email required")
parser.add_argument('password', required=True, help="Password required")


user_bp = Blueprint("user_bp", __name__)
api = Api(user_bp)


class Index(Resource):
    def get(self):
        return {"success": True, "message": "Hello World"}


class Users(Resource):
    def get(self):
        users_lc = [user.to_dict() for user in User.query.all()]

        return make_response(jsonify(users_lc), 200)

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


class UserById(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        return make_response(jsonify(user.to_dict()), 200)

    def patch(self, user_id):
        data = request.get_json()

        user = User.query.filter_by(id=user_id).first()

        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        for attr in data:
            setattr(user, attr, data.get(attr))

        db.session.commit()

        return make_response(jsonify(user.to_dict()), 200)

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        db.session.delete(user)
        db.session.commit()

        return make_response(jsonify({"success": True, "message": "User deleted successfully"}))


api.add_resource(Index, "/")
api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<int:user_id>")
