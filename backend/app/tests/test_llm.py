def test_api_mode(client):
    response = client.post("/llm/generate", json={"prompt": "Hello!", "mode": "api"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_local_mode(client):
    response = client.post("/llm/generate", json={"prompt": "Hello!", "mode": "local"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_dynamic_mode(client):
    client.post("/llm/start-dynamic")
    response = client.post("/llm/generate", json={"prompt": "Hello!", "mode": "dynamic"})
    assert response.status_code == 200
    assert "response" in response.json()
    client.post("/llm/stop-dynamic")
