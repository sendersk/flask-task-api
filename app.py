from flask import Flask, jsonify, request
from storage import add_task, get_task, get_all_tasks, update_task, delete_task

def create_app():
    app = Flask(__name__)

    # Health check endpoint
    @app.route("/ping", methods=["GET"])
    def ping():
        return jsonify({"message": "pong"}), 200

    # Create a new task
    @app.route("/tasks", methods=["POST"])
    def create_task():
        data = request.get_json()
        if not data or "title" not in data or "description" not in data:
            return jsonify({"error": "Missing required fields: title, description"}), 400

        status = data.get("status", "todo")
        try:
            task = add_task(data["title"], data["description"], status)
            return jsonify(task.to_dict()), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    # Get all tasks
    @app.route("/tasks", methods=["GET"])
    def list_tasks():
        tasks = get_all_tasks()
        return jsonify([t.to_dict() for t in tasks]), 200

    # Get single task by id
    @app.route("/tasks/<int:task_id>", methods=["GET"])
    def get_single_task(task_id):
        task = get_task(task_id)
        if task:
            return jsonify(task.to_dict()), 200
        return jsonify({"error": "Task not found"}), 404

    # Update task
    @app.route("/tasks/<int:task_id>", methods=["PUT"])
    def update_single_task(task_id):
        data = request.get_json()
        if not data:
            return jsonify({"error": " No update data provided"}), 400
        try:
            task = update_task(task_id, data)
            if task:
                return jsonify(task.to_dict()), 200
            return jsonify({"error": "Task not found"}), 404
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    # Delete task
    @app.route("/tasks/<int:task_id>", methods=["DELETE"])
    def delete_single_task(task_id):
        if delete_task(task_id):
            return jsonify({"message": "Task deleted"}), 200
        return jsonify({"error": "Task not found"}), 404

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
