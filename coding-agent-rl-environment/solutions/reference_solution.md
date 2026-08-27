# Reference Solution

The bug is caused by treating `discount_percent` as a fixed monetary
amount instead of a percentage.

The correct calculation is:

```python
discount_amount = subtotal * (discount_percent / 100)

total = subtotal - discount_amount + shipping + tax