# 11.2 -- from import: extrair um nome

## Conceito

`import math` traz o módulo *inteiro* e acedes-lhe através de
`math.something`. Muitas vezes só queres uma ferramenta, usada pelo seu nome simples. A
forma **`from ... import ...`** faz isso:

```python
from math import gcd

gcd(12, 18)      # 6  -- called directly, no math. prefix
```

- `from math import gcd` associa o nome único `gcd` ao teu ficheiro.
- Depois chamas-lo como `gcd(...)`, não como `math.gcd(...)`.
- Podes extrair vários de uma vez: `from math import gcd, sqrt, pi`.

`gcd(a, b)` é o **máximo divisor comum** -- o maior inteiro que
divide ambos. É exatamente o que precisas para simplificar uma fração aos
seus termos mais simples: divide o numerador e o denominador pelo seu gcd.

## Exemplo

```python
from math import gcd

def both_divisible_by(a, b):
    return gcd(a, b)
```

## A tua tarefa

Usando **`from math import gcd`**, define `simplify(num, den)` que devolve a
fração `num/den` simplificada aos termos mais simples, como um tuplo `(top, bottom)`: divide
`num` e `den` pelo respetivo `gcd`.

## Está feito quando

- `simplify(6, 8)` devolve `(3, 4)`, `simplify(10, 5)` devolve `(2, 1)`.
- `simplify(7, 7)` devolve `(1, 1)`.
- O gcd vem de `math`, importado com `from math import gcd`.
