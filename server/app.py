from config import app
from controllers.user_controllers import user_bp
from controllers.auth_controllers import auth_bp


# will register blueprints here
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp, url_prefix="auth/")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
