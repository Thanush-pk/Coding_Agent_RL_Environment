from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_percentage_discount_calculation():
    response = client.get("/orders/999/total")

    assert response.status_code == 200

    data = response.json()

    subtotal = data["subtotal"]
    discount_percent = data["discount_percent"]
    shipping = data["shipping"]
    tax = data["tax"]

    expected_total = (
        subtotal
        - (subtotal * discount_percent / 100)
        + shipping
        + tax
    )

    assert data["total"] == expected_total