from api.app import app

client = app.test_client()


def test_home():
    res = client.get("/")
    assert res.status_code == 200
    assert "message" in res.get_json()


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"


def test_recommend():
    res = client.get("/recommend/u1")
    assert res.status_code == 200
    data = res.get_json()
    assert "recommendations" in data


def test_feedback_get():
    res = client.get("/feedback")
    assert res.status_code == 200
    assert "message" in res.get_json()


def test_feedback_post():
    res = client.post("/feedback", json={
        "user_id": "u1",
        "content_id": "c10",
        "rating": 5
    })
    assert res.status_code == 200
    assert "status" in res.get_json()


def test_feedback_bad_request():
    res = client.post("/feedback", json={})
    assert res.status_code == 400


def test_metrics():
    res = client.get("/metrics")
    assert res.status_code == 200
    data = res.get_json()
    assert "total_requests" in data
    