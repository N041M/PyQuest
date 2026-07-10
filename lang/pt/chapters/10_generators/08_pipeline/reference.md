A peça de resistência compõe geradores num **pipeline em fluxo**: um
gerador **fonte** alimenta um gerador **filtro**, que alimenta um gerador
**transformação**. Cada etapa é preguiçosa, por isso os valores fluem um de
cada vez e nada é materializado por completo.

- Porque cada etapa consome a anterior de forma preguiçosa, o pipeline
  processa dados enormes ou infinitos com memória mínima — está apenas um
  item em trânsito de cada vez.
- As etapas mantêm-se pequenas e independentes: troca ou acrescenta uma
  etapa sem tocar nas outras. Este é o equivalente, em geradores, de compor
  funções.

```python
def reader(nums):  yield from nums
def keep_pos(src): yield from (n for n in src if n > 0)
def doubled(src):  yield from (n * 2 for n in src)

list(doubled(keep_pos(reader([-1, 2, -3, 4]))))   # [4, 8]
```
