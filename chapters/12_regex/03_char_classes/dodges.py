DODGES = [
    ("counts vowels with a membership loop, never importing re",
     "def count_vowels(text):\n"
     "    return sum(1 for c in text if c in 'aeiou')\n"),
]
