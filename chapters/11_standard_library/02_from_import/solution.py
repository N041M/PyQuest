from math import gcd


def simplify(num, den):
    g = gcd(num, den)
    return (num // g, den // g)
