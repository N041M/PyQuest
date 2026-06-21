from engine.inputs import random_word, random_int


def check(T):
    empty = T.make("Cart")
    T.eq(T.method(empty, "total"), 0, because="an empty cart totals 0.")

    cart = T.make("Cart")
    T.method(cart, "add", "Apple", 1.5)
    T.method(cart, "add", "Bread", 2.0)
    T.approx(T.method(cart, "total"), 3.5, because="1.5 + 2.0 = 3.5.")

    for _ in range(8):
        prices = [random_int(0, 5000) / 100 for _ in range(random_int(1, 6))]
        c = T.make("Cart")
        for pr in prices:
            T.method(c, "add", random_word(3, 6), pr)
        T.approx(T.method(c, "total"), sum(prices),
                 because="total is the sum of every added price.")
