Começa o ficheiro com `from math import gcd`. Agora `gcd` é uma função que podes chamar
diretamente, sem `math.` à frente.

---

Calcula `g = gcd(num, den)`, depois devolve o tuplo `(num // g, den // g)`. Usa `//`
(divisão inteira) para que o resultado fique em números inteiros.

---

from math import gcd


def simplify(num, den):
    g = gcd(num, den)
    return (num // g, den // g)
