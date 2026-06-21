from engine.inputs import random_word, random_int


def check(T):
    apple = T.make("Item", "Apple", 1.5)
    T.eq(T.attr(apple, "name"), "Apple")
    T.eq(T.attr(apple, "price"), 1.5)
    T.eq(T.method(apple, "label"), "Apple: $1.50")
    T.eq(T.method(T.make("Item", "Bread", 2), "label"), "Bread: $2.00")
    for _ in range(8):
        name = random_word(3, 7).capitalize()
        cents = random_int(0, 9999)
        price = cents / 100
        item = T.make("Item", name, price)
        T.eq(T.method(item, "label"), "%s: $%.2f" % (name, price),
             because="label is 'name: $price' to 2 decimals.")
