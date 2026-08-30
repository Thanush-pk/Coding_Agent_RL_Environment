from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_basic_order_calculation():
    response = client.post(
        "/orders/calculate",
        json={
            "items": [
                {
                    "product_id": 1,
                    "name": "Laptop",
                    "price": 1000,
                    "quantity": 1,
                    "discount_eligible": True,
                }
            ],
            "discount_percent": 10,
            "shipping": 20,
            "tax_percent": 10,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["subtotal"] == 1000
    assert data["discount"] == 100
    assert data["tax"] == 90
    assert data["shipping"] == 20
    assert data["total"] == 1010


def test_non_eligible_item_does_not_receive_discount():
    response = client.post(
        "/orders/calculate",
        json={
            "items": [
                {
                    "product_id": 1,
                    "name": "Laptop",
                    "price": 1000,
                    "quantity": 1,
                    "discount_eligible": True,
                },
                {
                    "product_id": 2,
                    "name": "Warranty",
                    "price": 200,
                    "quantity": 1,
                    "discount_eligible": False,
                },
            ],
            "discount_percent": 10,
            "shipping": 20,
            "tax_percent": 10,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["subtotal"] == 1200

    # Only the laptop receives the 10% discount.
    assert data["discount"] == 100

    # Tax is calculated after discount.
    assert data["tax"] == 110

    assert data["total"] == 1230