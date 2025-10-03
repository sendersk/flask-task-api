from flask import request, jsonify, render_template, redirect, url_for
from utils import validate_task_input
import storage


def register_routes(app):
    """Attach API and GUI routes to the Flask app."""

    # ----------------------
    # API ROUTES (JSON)
    # ----------------------

    @app.route("/tasks", methods=["GET"])
    def get_tasks():
        return jsonify([t.to_dict() for t in storage.get_all_tasks()])

    @app.route("/tasks/<int:task_id>", methods=["GET"])
    def get_single_task(task_id):
        task = storage.get_task(task_id)
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

        task = storage.add_task(
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

        task = storage.update_task(task_id, data)
        if task:
            return jsonify(task.to_dict()), 200
        return jsonify({"error": "Task not found"}), 404

    @app.route("/tasks/<int:task_id>", methods=["DELETE"])
    def delete_single_task(task_id):
        task = storage.delete_task(task_id)
        if task:
            return jsonify({"message": "Task deleted"}), 200
        return jsonify({"error": "Task not found"}), 404

    # ----------------------
    # GUI ROUTES (HTML)
    # ----------------------

    @app.route("/")
    def index():
        """Render the main task list page."""
        tasks = storage.get_all_tasks()
        return render_template("index.html", tasks=tasks)

    @app.route("/add", methods=["GET", "POST"])
    def add_task_gui():
        """Form for adding a new task."""
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            storage.add_task(title=title, description=description)
            return redirect(url_for("index"))
        return render_template("add.html")

    @app.route("/edit/<int:task_id>", methods=["GET", "POST"])
    def edit_task_gui(task_id):
        """Form for editing an existing task."""
        task = storage.get_task(task_id)
        if not task:
            return render_template("404.html"), 404

        if request.method == "POST":
            task.title = request.form["title"]
            task.description = request.form["description"]
            task.status = request.form["status"]
            return redirect(url_for("index"))

        return render_template("edit.html", task=task)

    @app.route("/delete/<int:task_id>")
    def delete_task_gui(task_id):
        """Delete a task from GUI."""
        storage.delete_task(task_id)
        return redirect(url_for("index"))
