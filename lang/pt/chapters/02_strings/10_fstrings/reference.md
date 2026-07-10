Uma **f-string** (literal de cadeia formatada) é uma cadeia prefixada com `f` na qual
`{ }` contém uma **expressão** Python; a expressão é avaliada e o seu valor é
inserido, convertido em texto.

- Qualquer expressão cabe dentro das chavetas: `f"{name}"`, `f"{a + b}"`,
  `f"{nums[0]}"`.
- Uma chaveta literal escreve-se duplicando-a: `f"{{literal}}"` mostra `{literal}`.
- Uma especificação de formato depois de dois pontos controla a apresentação, por exemplo,
  `f"{price:.2f}"` mostra duas casas decimais e `f"{n:>5}"` alinha à direita num campo
  com 5 de largura.

As f-strings são a forma mais clara de construir texto a partir de valores, substituindo cadeias de
`+` e `str()`.

```python
name, n = "Ada", 3
f"{name} solved {n} puzzles"   # 'Ada solved 3 puzzles'
f"{1/3:.2f}"                    # '0.33'
```
