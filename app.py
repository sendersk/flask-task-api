from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    # Health check endpoint
    @app.route("/ping", methods=["GET"])
    def ping():
        return jsonify({"message": "pong"}), 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
