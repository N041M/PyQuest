DODGES = [
    ("reduces with a hand-written Euclid loop, never importing gcd",
     "def simplify(num, den):\n"
     "    a, b = num, den\n"
     "    while b:\n"
     "        a, b = b, a % b\n"
     "    return (num // a, den // a)\n"),
]
