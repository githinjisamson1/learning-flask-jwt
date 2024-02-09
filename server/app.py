from config import app, api
from flask_restful import Resource


class Index(Resource):
    def get(self):
        return {"success": True, "message": "Hello World"}, 200


api.add_resource(Index, "/")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
