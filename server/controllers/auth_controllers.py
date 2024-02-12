from flask import Blueprint, make_response, jsonify, request
from flask_restful import Api, Resource, reqparse
from config import db, bcrypt
from models import User
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt, current_user, get_jwt_identity

# !will contain Register and Login resources
auth_bp = Blueprint("auth_bp", __name__)
api = Api(auth_bp)

# !user data
parser = reqparse.RequestParser()
parser.add_argument('username', required=True, help="Username required")
parser.add_argument('email', required=True, help="Email required")
parser.add_argument('password', required=True, help="Password required")


# !auth resources
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


class Login(Resource):
    def post(self):
        data = request.get_json()

        user = User.query.filter_by(username=data.get("username")).first()

        # if user exists and password matches
        if user and user.authenticate(data.get("password")):
            # access: for access + short-lived, refresh: for security + long-lived
            access_token = create_access_token(identity=user.username)
            refresh_token = create_refresh_token(identity=user.username)

            # generate token-pair:{access, refresh}
            return make_response(jsonify({
                "message": "Login successful",
                "tokens": {
                    "access": access_token,
                    "refresh": refresh_token
                }
            }), 200)

        return make_response(jsonify({"error": "Invalid username or password"}), 401)


class Whoami(Resource):
    @jwt_required()
    def get(self):
        # TODO: !returns jwt claims as python dictionary i.e., payload for e.g., johndoe
        # claims = get_jwt()
        # return make_response(jsonify({"message": "Whoami", "claims": claims}))

        # TODO: !automatic user loading
        return make_response(jsonify({"message": "Whoami", "user_details": {
            "username": current_user.username,
            "email": current_user.email,
            # "password":current_user._password_hash
        }}), 200)


class RefreshAccess(Resource):
    @jwt_required(refresh=True)
    def get(self):
        # similar to jwt_data["sub"] OR get_jwt()["sub"]
        identity = get_jwt_identity()
        new_access_token = create_access_token(identity=identity)
        return {"access_token": new_access_token}


class Logout(Resource):
    @jwt_required()
    def get(self):

        pass


api.add_resource(Register, "/register")
api.add_resource(Login, "/login")
api.add_resource(Whoami, "/whoami")
api.add_resource(RefreshAccess, "/refresh_access")
api.add_resource(Logout, "/logout")
