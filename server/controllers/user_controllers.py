from flask import Blueprint, make_response, jsonify, request
from flask_restful import Api, Resource, reqparse
from models import User
from config import db
from flask_jwt_extended import jwt_required


# user_bp
user_bp = Blueprint("user_bp", __name__)
api = Api(user_bp)


# resources
class Index(Resource):
    def get(self):
        return {"success": True, "message": "Hello World"}, 200


class Users(Resource):
    # @jwt_required() to protect routes
    @jwt_required()
    def get(self):
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=2, type=int)

        users = User.query.paginate(
            page=page,
            per_page=per_page
        )
        users_lc = [user.to_dict() for user in users]
        return make_response(jsonify(users_lc), 200)


class UserById(Resource):
    @jwt_required()
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        return make_response(jsonify(user.to_dict()), 200)

    @jwt_required()
    def patch(self, user_id):
        data = request.get_json()

        user = User.query.filter_by(id=user_id).first()

        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        for attr in data:
            setattr(user, attr, data.get(attr))

        db.session.commit()

        return make_response(jsonify(user.to_dict()), 200)

    @jwt_required()
    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        db.session.delete(user)
        db.session.commit()

        return make_response(jsonify({"success": True, "message": "User deleted successfully"}))


# URLs
api.add_resource(Index, "/")
api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<int:user_id>")
