As listas são **mutáveis**: o seu conteúdo pode ser alterado no próprio local,
ao contrário das cadeias de caracteres.

- **`lst[i] = x`** substitui o item no índice `i`. O índice já tem de existir
  (atribuir além do fim gera um `IndexError`).
- **`.pop()`** remove e **devolve** o último item, reduzindo a lista;
  `.pop(i)` remove o item no índice `i`. Fazer pop de uma lista vazia gera um erro.
- Outras alterações no próprio local: `.insert(i, x)`, `.remove(value)`, `del lst[i]`.

Como a alteração é feita no próprio local, qualquer nome que se refira ao mesmo
objeto lista vê-a.

```python
lst = [10, 20, 30]
lst[1] = 99      # [10, 99, 30]
last = lst.pop() # last == 30, lst == [10, 99]
```
