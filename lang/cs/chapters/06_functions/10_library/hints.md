count_vowels je sčítání přes znaky: cyklus `for ch in word` a test `ch in
"aeiou"`.

---

describe zavolá count_vowels jednou, uloží číslo, pak časně vrátí znění "no
vowels", když je 0; jinak f-řetězec s počtem.

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
