Dois métodos de procura e contagem:

- **`s.replace(old, new)`** devolve uma cadeia nova com **todas** as ocorrências
  não sobrepostas de `old` trocadas por `new`. Substitui todas as correspondências, não só a
  primeira; se `old` não ocorrer, a cadeia volta sem alterações.
- **`s.count(sub)`** devolve quantas vezes `sub` aparece, contando
  correspondências não sobrepostas da esquerda para a direita. `"aaa".count("aa")` é `1`, não 2.

Ambos apenas leem `s` e devolvem informação nova; a cadeia original permanece intocada.

```python
"a-b-c".replace("-", "_")   # 'a_b_c'  -- every match
"banana".count("a")          # 3
```
