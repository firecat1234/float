# tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_config_load(client):
    response = client.get("/config")  # Adjust based on your actual configuration endpoint
    assert response.status_code == 200
    config_data = response.json()
    assert "SQLALCHEMY_DATABASE_URI" in config_data
    assert "DEFAULT_MODEL" in config_data

def test_openapi_schema(client):
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert "/chat/" in schema["paths"]
    assert "/tools/" in schema["paths"]

def test_health_check(client):
    response = client.get("/health")  # Adjust based on your health check endpoint
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_invalid_endpoint(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404
