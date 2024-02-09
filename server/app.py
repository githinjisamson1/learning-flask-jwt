from config import app
from controllers.user_controllers import user_bp

# register blueprints
app.register_blueprint(user_bp, )

if __name__ == "__main__":
    app.run(port=5555, debug=True)
