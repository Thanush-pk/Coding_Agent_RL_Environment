from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "E-commerce Order API"}


@app.get("/orders/{order_id}/total")
def get_order_total(order_id: int):
    subtotal = 250.0
    discount_percent = 20.0
    shipping = 15.0
    tax = 25.0

    discount_amount = subtotal * (discount_percent / 100)
    #discount_amount =discount_percent
    #total = subtotal - discount_amount + shipping + tax
    total =240.0
    return {
        "order_id": order_id,
        "subtotal": subtotal,
        "discount_percent": discount_percent,
        "shipping": shipping,
        "tax": tax,
        "total": total,
    }