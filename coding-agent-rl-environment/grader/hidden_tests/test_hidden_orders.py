from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_multiple_items_mixed_eligibility():
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
                    "name": "Mouse",
                    "price": 50,
                    "quantity": 2,
                    "discount_eligible": False,
                },
                {
                    "product_id": 3,
                    "name": "Keyboard",
                    "price": 100,
                    "quantity": 1,
                    "discount_eligible": True,
                },
            ],
            "discount_percent": 20,
            "shipping": 30,
            "tax_percent": 10,
        },
    )

    assert response.status_code == 200

    data = response.json()

    # Subtotal = 1000 + 100 + 100 = 1200
    assert data["subtotal"] == 1200

    # Eligible subtotal = 1000 + 100 = 1100
    # Discount = 1100 * 20% = 220
    assert data["discount"] == 220

    # Taxable = 1200 - 220 = 980
    # Tax = 98
    assert data["tax"] == 98

    # Total = 1200 - 220 + 98 + 30
    assert data["total"] == 1108


def test_all_items_non_eligible():
    response = client.post(
        "/orders/calculate",
        json={
            "items": [
                {
                    "product_id": 1,
                    "name": "Warranty",
                    "price": 200,
                    "quantity": 2,
                    "discount_eligible": False,
                },
                {
                    "product_id": 2,
                    "name": "Service",
                    "price": 100,
                    "quantity": 1,
                    "discount_eligible": False,
                },
            ],
            "discount_percent": 50,
            "shipping": 10,
            "tax_percent": 10,
        },
    )

    assert response.status_code == 200

    data = response.json()

    # No item is eligible, therefore discount = 0.
    assert data["discount"] == 0

    # Subtotal = 400 + 100 = 500
    assert data["subtotal"] == 500

    # Tax = 500 * 10% = 50
    assert data["tax"] == 50

    # Total = 500 + 50 + 10
    assert data["total"] == 560


def test_quantity_affects_discount():
    response = client.post(
        "/orders/calculate",
        json={
            "items": [
                {
                    "product_id": 1,
                    "name": "Headphones",
                    "price": 100,
                    "quantity": 3,
                    "discount_eligible": True,
                },
                {
                    "product_id": 2,
                    "name": "Cable",
                    "price": 20,
                    "quantity": 2,
                    "discount_eligible": False,
                },
            ],
            "discount_percent": 10,
            "shipping": 5,
            "tax_percent": 10,
        },
    )

    assert response.status_code == 200

    data = response.json()

    # Eligible subtotal = 100 * 3 = 300
    assert data["discount"] == 30

    # Total subtotal = 300 + 40 = 340
    assert data["subtotal"] == 340

    # Taxable = 340 - 30 = 310
    assert data["tax"] == 31

    # Total = 340 - 30 + 31 + 5
    assert data["total"] == 346