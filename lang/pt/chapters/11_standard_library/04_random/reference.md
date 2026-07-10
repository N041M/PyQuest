O módulo **`random`** gera valores pseudoaleatórios a partir de um estado
interno: `random.randint(a, b)` (um inteiro em `[a, b]`), `random.choice(seq)`
(um item aleatório), `random.shuffle(lst)` (reordena uma lista **no próprio
local**), `random.random()` (um float em `[0, 1)`).

- Os números são funções determinísticas do estado, por isso
  **`random.seed(n)`** torna-os **repetíveis**: com a mesma seed, as mesmas
  chamadas dão os mesmos resultados em toda a execução e máquina. Define a
  seed uma vez, antes dos sorteios que queres reproduzir.
- `random.shuffle` altera o seu argumento e devolve `None` — baralha uma
  **cópia** (`out = list(items)`) para manter o original, e nunca faças
  `return random.shuffle(...)`.
- O gerador por omissão (sem seed) recebe a seed a partir do sistema
  operativo, por isso, sem uma seed, cada execução é diferente. O `random`
  **não** é para criptografia — usa o módulo `secrets` para tokens e
  palavras-passe.

```python
import random

random.seed(42)
random.randint(1, 6)     # same value every run for seed 42
deck = [1, 2, 3, 4]
random.shuffle(deck)     # deck reordered in place
```
