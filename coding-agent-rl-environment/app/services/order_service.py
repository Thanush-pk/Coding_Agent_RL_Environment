from app.services.discount_service import calculate_discount
from app.services.tax_service import calculate_tax


def calculate_order_total(order):
    subtotal = sum(
        item.price * item.quantity
        for item in order.items
    )

    discount = calculate_discount(
        order.items,
        order.discount_percent,
    )

    taxable_amount = subtotal - discount

    tax = calculate_tax(
        taxable_amount,
        order.tax_percent,
    )

    total = (
        subtotal
        - discount
        + tax
        + order.shipping
    )

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "shipping": order.shipping,
        "total": total,
    }