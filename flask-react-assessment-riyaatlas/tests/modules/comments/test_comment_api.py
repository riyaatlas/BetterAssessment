import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_comment(client):
    data = {"task_id": "task123", "author_id": "user123", "content": "This is a test comment"}
    response = client.post("/api/comments", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 201
    assert response.json["content"] == "This is a test comment"

def test_get_comments_by_task(client):
    response = client.get("/api/comments/task/task123")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_update_comment(client):
    # Create comment first
    data = {"task_id": "task123", "author_id": "user123", "content": "Old content"}
    response = client.post("/api/comments", data=json.dumps(data), content_type="application/json")
    comment_id = response.json["id"]

    # Update
    update_data = {"content": "Updated content"}
    response = client.patch(f"/api/comments/{comment_id}", data=json.dumps(update_data), content_type="application/json")
    assert response.status_code == 200
    assert response.json["content"] == "Updated content"

def test_delete_comment(client):
    # Create comment
    data = {"task_id": "task123", "author_id": "user123", "content": "To be deleted"}
    response = client.post("/api/comments", data=json.dumps(data), content_type="application/json")
    comment_id = response.json["id"]

    # Delete
    response = client.delete(f"/api/comments/{comment_id}")
    assert response.status_code == 204
