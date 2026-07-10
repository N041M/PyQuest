`print` escreve uma representação textual de cada argumento na saída padrão (o
terminal), por ordem, e depois escreve `end` (uma quebra de linha por omissão). É a
forma principal de um programa mostrar um resultado ao utilizador.

- Cada valor é primeiro convertido em texto com `str()`, por isso `print(42)` e
  `print("42")` mostram ambos `42`.
- Com vários argumentos, `sep` (por omissão um único espaço) é colocado *entre*
  valores adjacentes -- nunca antes do primeiro nem depois do último.
- `end` é acrescentado uma vez, depois de tudo o resto. Como o valor por omissão é `"\n"`,
  cada chamada a `print` termina a linha atual e o resultado seguinte começa de novo.
- `print` devolve `None`; é chamado pelo seu efeito, não pelo seu valor.

```python
print("Hello, World!")        # Hello, World!
print("a", "b", "c")          # a b c
```
