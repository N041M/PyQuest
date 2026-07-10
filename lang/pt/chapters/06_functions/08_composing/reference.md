As funções **chamam outras funções**, por isso uma tarefa maior é construída a partir de peças
pequenas e testadas. O resultado de uma torna-se o argumento ou bloco de construção da seguinte.

- Um auxiliar faz bem um trabalho; uma função de nível superior chama vários auxiliares e
  combina os seus resultados. Isto é o cerne de estruturar um programa.
- `f(g(x))` alimenta o resultado de `g` diretamente para `f`. Cada função mantém-se simples e
  verificável de forma independente.

```python
def clean(s):  return s.strip().lower()
def is_yes(s): return clean(s) == "yes"

is_yes("  YES ")   # True  -- is_yes builds on clean
```
