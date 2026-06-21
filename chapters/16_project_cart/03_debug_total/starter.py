# Puzzle 16.3 -- Debug: the discount is wrong
# Project: Shopping Cart (step 3 of 4)
#
# This code is written but BUGGY. Find and fix discounted_total so a `percent`
# discount is applied correctly. Don't change the other methods.

class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        self.items.append((name, price))

    def total(self):
        return sum(price for name, price in self.items)

    def discounted_total(self, percent):
        # BUG: this subtracts `percent` as if it were dollars, not a percentage.
        return self.total() - percent
