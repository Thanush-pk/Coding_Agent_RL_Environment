from fastapi import FastAPI

from app.models.order import Order
from app.services.order_service import calculate_order_total


app = FastAPI(
    title="OrderFlow API",
    description="E-commerce order calculation API",
)


@app.get("/")
def root():
    return {
        "message": "OrderFlow API",
        "version": "1.0.0",
    }


@app.post("/orders/calculate")
def calculate_order(order: Order):
    return calculate_order_total(order)