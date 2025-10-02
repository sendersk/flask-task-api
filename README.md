# Flask Task API

A lightweight Flask-based REST API for managing tasks.

---

## Navigation

- [Overview](#overview)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Setup](#setup)
- [Technologies](#technologies)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## Overview

This project provides a simple task management API built with Flask.
It allows creating, retrieving, updating, and deleting tasks using JSON-based HTTP requests.
Storage is in-memory for simplificity, making it ideal for prototyping.

---

## Project Structure

```
flask_task_api/
│
├── main.py           # Entry point, initializes Flask app (includes GUI + API)
├── routes.py         # API routes (endpoints)
├── models.py         # Task model (structure and validation)
├── storage.py        # In-memory storage logic
├── utils.py          # Helper functions (e.g., input validation)
├── tests.py          # Unit tests for API
│
├── templates/        # Jinja2 templates for GUI
│   ├── base.html     # Shared layout
│   ├── index.html    # Task list
│   ├── add.html      # Add task form
│   └── edit.html     # Edit task form
│
├── static/           # Static assets
│   └── style.css     # Basic styling
│
├── requirements.txt  # Dependencies (Flask, etc.)
├── README.md         # Project documentation
└── .gitignore        # Ignore venv, etc.
```

---

## API Endpoints

- `GET /ping` → Health check
- `GET /tasks` → Get all tasks
- `GET /tasks/<id>` → Get a task by ID
- `POST /tasks` → Create a task
- `PUT /tasks/<id>` → Update a task
- `DELETE /tasks/<id>` → Delete a task

---

## Setup
```bash
# Clone the repository
git clone https://github.com/sendersk/flask-task-api.git
cd flask-task-api

# Create virtual environment
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py

```

## Technologies

- Python
- Flask
- REST API
- JSON

---

## Future Improvements

- Save tasks to JSON file or database
- Add authentication

---

## Author
Created by **Przemysław Senderski**