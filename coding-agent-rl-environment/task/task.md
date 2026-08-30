# Fix Order Total Calculation

The order total calculation is incorrect when a percentage discount is applied.

The `discount_percent` value should represent a percentage of the subtotal.

For example:

- Subtotal: 250
- Discount: 20%
- Shipping: 15
- Tax: 25

The expected total is:

250 - (250 × 0.20) + 15 + 25 = 240

Fix the implementation so that the order total is calculated correctly.

Requirements:

- Preserve the existing API endpoint.
- Preserve the existing response structure.
- `discount_percent` must be treated as a percentage.
- Do not hardcode the expected total.
- Existing functionality must continue to work.