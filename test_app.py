import pytest
from main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_create_task_success(client):
    response = client.post("/tasks", json={
        "title": "Test Task",
        "description": "Some description"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Test Task"
    assert data["status"] == "todo"


def test_create_task_invalid(client):
    response = client.post("/tasks", json={
        "title": "ab",
        "description": ""
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "errors" in data


def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_update_nonexistent_task(client):
    response = client.put("/tasks/999", json={"status": "done"})
    assert response.status_code == 404


def test_delete_task(client):
    # Create a task
    create_response = client.post("/tasks", json={
        "title": "Delete Me",
        "description": "Will be deleted"
    })
    task_id = create_response.get_json()["id"]

    # Delete it
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200

    # Verify it's gone
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
