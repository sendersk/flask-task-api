from flask import Flask
from routes import register_routes

# Initialize Flask app
app = Flask(__name__)

# Register all routes (API + GUI)
register_routes(app)

if __name__ == "__main__":
    # Run app in debug mode
    app.run(debug=True)
