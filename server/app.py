from config import app
from controllers.user_controllers import user_bp


# will register blueprints here
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
