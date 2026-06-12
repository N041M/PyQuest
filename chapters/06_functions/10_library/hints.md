count_vowels is a tally over the characters: loop with `for ch in word` and
test `ch in "aeiou"`.

---

describe calls count_vowels once, stores the number, then early-returns the
"no vowels" wording when it is 0; otherwise an f-string with the count.

---

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
