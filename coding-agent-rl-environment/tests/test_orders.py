from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "E-commerce Order API"


def test_order_total():
    response = client.get("/orders/123/total")

    assert response.status_code == 200

    data = response.json()

    assert data["total"] == 240.0