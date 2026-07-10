Os conjuntos suportam a álgebra de coleções:

- **`a & b`** (interseção) — itens em **ambos**.
- **`a | b`** (união) — itens em **qualquer um**.
- **`a - b`** (diferença) — itens em `a` mas **não** em `b`.

Cada uma devolve um **novo** conjunto. (`^` é a diferença simétrica — em
exatamente um.) Estas expressam perguntas sobre conjuntos diretamente,
substituindo ciclos escritos à mão que comparam duas coleções.

```python
a, b = {1, 2, 3}, {2, 3, 4}
a & b     # {2, 3}
a | b     # {1, 2, 3, 4}
a - b     # {1}
```
