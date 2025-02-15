from fastapi.testclient import TestClient
from backend.main import app
from app import database

client = TestClient(app)

def test_create_file():
    response = client.post("/files/", json={"name": "test.pdf", "path": "/test/test.pdf", "type": "pdf", "size": 1024})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test.pdf"
    assert data["path"] == "/test/test.pdf"
    assert data["type"] == "pdf"
    assert data["size"] == 1024

def test_read_file():
    response = client.post("/files/", json={"name": "test.pdf", "path": "/test/test.pdf", "type": "pdf", "size": 1024})
    file_id = response.json()["id"]
    response = client.get(f"/files/{file_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == file_id
    assert data["name"] == "test.pdf"