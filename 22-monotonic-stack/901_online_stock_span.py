class StockSpanner:
    def __init__(self):
        self.prices = []  # List to store stock prices
        self.spans = []  # List to store spans
        self.stack = []  # Monotonic stack to store indices

    def next(self, price: int) -> int:
        # Calculate the span for the current price
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()  # Pop indices of prices less than or equal to the current price

        span = (
            len(self.prices) + 1
            if not self.stack
            else len(self.prices) - self.stack[-1]
        )

        # Add the current price and its index
        self.prices.append(price)
        self.spans.append(span)
        self.stack.append(len(self.prices) - 1)  # Push the current index onto the stack

        return span
