# tests/test_chat.py
import pytest
from main import create_app
from models.database import db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_chat_endpoint(client):
    response = client.post("/chat/", json={
        "message": "Hello, Gemini!",
        "session_id": "test-session",
        "use_rag": True
    })
    assert response.status_code == 200
    assert "message" in response.json()
    assert "thought" in response.json()
    # Ensure all metadata fields are present
    assert "metadata" in response.json()
    metadata = response.json()["metadata"]
    assert "timestamp" in metadata
    assert "model_used" in metadata
    assert metadata["model_used"] == "default-model"

def test_chat_invalid_input(client):
    # Test for empty message
    response = client.post("/chat/", json={"message": ""})
    assert response.status_code == 422  # Unprocessable Entity

    # Test for missing required fields
    response = client.post("/chat/", json={})
    assert response.status_code == 422

    # Test for malformed data
    response = client.post("/chat/", data="Not JSON")
    assert response.status_code == 400
