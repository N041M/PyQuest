A primeiríssima linha do ficheiro torna o módulo disponível: `import math`. A partir
daí podes usar tudo o que ele fornece como `math.something`.

---

`math.sqrt(x)` devolve a raiz quadrada de `x`. Queres a raiz quadrada de
`a*a + b*b`. Coloca o `import math` no topo e depois escreve a função.

---

import math


def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)
