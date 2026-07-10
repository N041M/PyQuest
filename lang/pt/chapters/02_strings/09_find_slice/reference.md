**`s.find(sub)`** devolve o índice da **primeira** ocorrência de `sub` em `s`,
ou **`-1`** se não for encontrado (nunca gera erro). Combiná-lo com fatiamento extrai
o texto à volta de um marcador.

- O índice devolvido é onde `sub` começa, por isso `s[:i]` é a parte antes dele e
  `s[i + len(sub):]` a parte depois.
- Verifica se é `-1` antes de usar o resultado — caso contrário, um `s.find` que
  devolva `-1` fatiaria a partir do fim.
- `.index(sub)` é semelhante mas **gera** `ValueError` quando ausente; usa `.find`
  quando "não estar presente" é um caso normal.

```python
s = "key=value"
i = s.find("=")     # 3
s[:i]               # 'key'
s[i + 1:]           # 'value'
```
