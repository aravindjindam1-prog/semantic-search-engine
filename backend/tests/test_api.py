from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_search():
    response = client.post("/search", json={"query": "semantic search", "top_k": 2})
    assert response.status_code == 200
    assert "results" in response.json()
