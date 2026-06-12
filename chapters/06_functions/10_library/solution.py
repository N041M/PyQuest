def count_vowels(word):
    count = 0
    for ch in word:
        if ch in "aeiou":
            count = count + 1
    return count


def describe(word):
    n = count_vowels(word)
    if n == 0:
        return f"{word} has no vowels"
    return f"{word} has {n} vowels"
