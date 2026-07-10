**`sep.join(parts)`** cola um iterável de **cadeias de caracteres** numa só cadeia,
colocando `sep` entre itens adjacentes. O separador é a cadeia sobre a qual se
chama o método, o que parece estranho à primeira vista mas permite que o separador
seja qualquer cadeia de caracteres.

- Cada item já tem de ser uma cadeia de caracteres; números geram `TypeError`.
  Converte primeiro, por exemplo `", ".join(str(n) for n in nums)`.
- `"".join(parts)` concatena sem separador — a forma eficiente de construir uma
  cadeia a partir de muitas partes (muito melhor do que `+` repetido).
- É o inverso de `split`.

```python
"-".join(["2024", "01", "15"])   # '2024-01-15'
" ".join(["the", "fox"])          # 'the fox'
```
