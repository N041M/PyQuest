class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def label(self):
        return "%s: $%.2f" % (self.name, self.price)
