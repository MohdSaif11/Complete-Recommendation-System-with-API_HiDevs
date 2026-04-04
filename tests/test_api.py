import json
from api.app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200

def test_recommend():
    client = app.test_client()
    response = client.get("/recommend/u1")

    assert response.status_code == 200
    data = json.loads(response.data)

    assert "recommendations" in data

def test_feedback():
    client = app.test_client()

    response = client.post("/feedback", json={
        "user_id": "u1",
        "content_id": "c1",
        "rating": 5
    })

    assert response.status_code == 200