from pydantic import BaseModel, Field


class OrderItem(BaseModel):
    product_id: int
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)
    discount_eligible: bool = True


class Order(BaseModel):
    items: list[OrderItem]
    discount_percent: float = Field(default=0, ge=0, le=100)
    shipping: float = Field(default=0, ge=0)
    tax_percent: float = Field(default=10, ge=0, le=100)