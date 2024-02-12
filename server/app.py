from config import app, jwt
from controllers.user_controllers import user_bp
from controllers.auth_controllers import auth_bp
from flask import make_response, jsonify
from models import User, TokenBlocklist


# !will register blueprints here
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp, url_prefix="/auth")


# !automatic user loading
@jwt.user_lookup_loader
def user_lookup_callback(jwt_header, jwt_data):
    # jwt_data => actual claims
    identity = jwt_data["sub"]

    # query SQLAlchemy
    return User.query.filter_by(username=identity).one_or_none()


# !additional claims == no need to query db to check if staff or not
# adding attributes to existing payload
@jwt.additional_claims_loader
def make_additional_claims(identity):
    if identity == "johndoe":
        return {"is_staff": True}
    return {"is_staff": False}


# !jwt error handlers => handle invalid, missing, expired tokens
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return make_response(jsonify({
        "message": "Token has expired",
        "error": "token_expired"
    }), 400)


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return make_response(jsonify({
        "message": "Signature verification failed",
        "error": "token_invalid"
    }), 401)


@jwt.unauthorized_loader
def missing_token_callback(error):
    return make_response(jsonify({
        "message": "Request does not contain valid token",
        "error": "authorization_header"
    }), 401)


@jwt.token_in_blocklist_loader
def token_in_blocklist_callback(jwt_header, jwt_data):
    # jtw_data == claims9 == get_jwt() == contains hidden or encoded info/info about out token
    jti = jwt_data["jti"]

    token = TokenBlocklist.query.filter_by(jti=jti).first()

    return True if token else False
    # return token is not None


if __name__ == "__main__":
    app.run(port=5555, debug=True)
