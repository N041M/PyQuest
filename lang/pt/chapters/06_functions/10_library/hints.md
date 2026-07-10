count_vowels é uma contagem sobre os caracteres: percorre com `for ch in word` e
testa `ch in "aeiou"`.

---

describe chama count_vowels uma vez, guarda o número, depois faz um retorno antecipado com o
texto de "no vowels" quando é 0; caso contrário, uma f-string com a contagem.

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
