from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    response_body = {
        "success": True,
        "message": "Hello world"
    }

    response = make_response(jsonify(response_body), 200)

    response.headers["Content-Type"] = "application/json"

    return response


if __name__ == "__main__":
    app.run(port=5555, debug=True)
