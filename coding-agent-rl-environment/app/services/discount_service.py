def calculate_discount(items, discount_percent):
    eligible_subtotal = sum(
        item.price * item.quantity
        for item in items
        if item.discount_eligible
    )

    return eligible_subtotal * (discount_percent / 100)