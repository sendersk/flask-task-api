from flask import Flask, request, jsonify
from utils import validate_task_input

# In-memory storage for tasks
tasks = {}
next_id = 1

# Flask app
app = Flask(__name__)


class Task:
    """Simple Task model stored in memory."""

    def __init__(self, id, title, description, status="todo"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
        }


# Helper functions
def add_task(title, description, status="todo"):
    global next_id
    task = Task(next_id, title, description, status)
    tasks[next_id] = task
    next_id += 1
    return task


def get_task(task_id):
    return tasks.get(task_id)


def update_task(task_id, data):
    task = tasks.get(task_id)
    if not task:
        return None
    if "title" in data:
        task.title = data["title"]
    if "description" in data:
        task.description = data["description"]
    if "status" in data:
        task.status = data["status"]
    return task


def delete_task(task_id):
    return tasks.pop(task_id, None)


# Routes
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify([t.to_dict() for t in tasks.values()])


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_single_task(task_id):
    task = get_task(task_id)
    if task:
        return jsonify(task.to_dict())
    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    errors = validate_task_input(data)
    if errors:
        return jsonify({"errors": errors}), 400

    task = add_task(
        title=data["title"],
        description=data["description"],
        status=data.get("status", "todo"),
    )
    return jsonify(task.to_dict()), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_single_task(task_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No update data provided"}), 400

    errors = validate_task_input(data)
    if errors:
        return jsonify({"errors": errors}), 400

    task = update_task(task_id, data)
    if task:
        return jsonify(task.to_dict()), 200
    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_single_task(task_id):
    task = delete_task(task_id)
    if task:
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
