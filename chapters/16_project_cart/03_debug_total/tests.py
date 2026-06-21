from engine.inputs import random_int


def check(T):
    # the reported case: 10% off a $50 cart must be 45, not 40
    c = T.make("Cart")
    T.method(c, "add", "Widget", 50.0)
    T.approx(T.method(c, "discounted_total", 10), 45.0,
             because="10% off $50 is $45.")
    T.approx(T.method(c, "discounted_total", 0), 50.0,
             because="0% discount leaves the total unchanged.")

    for _ in range(8):
        prices = [random_int(0, 5000) / 100 for _ in range(random_int(1, 6))]
        percent = random_int(0, 90)
        cart = T.make("Cart")
        for pr in prices:
            T.method(cart, "add", "x", pr)
        total = sum(prices)
        T.approx(T.method(cart, "discounted_total", percent),
                 total * (1 - percent / 100),
                 because="discounted_total(%d) on total %.2f is %.2f."
                         % (percent, total, total * (1 - percent / 100)))
