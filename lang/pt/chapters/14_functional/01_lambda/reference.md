Uma **`lambda`** é uma função anónima escrita como uma única expressão:
`lambda args: expression`. O valor da expressão é devolvido automaticamente —
não há `return`, e o corpo tem de ser **uma** expressão.

- Uma lambda é um **valor** de primeira classe: atribui-a, devolve-a, ou
  passa-a como argumento. `f = lambda x: x * 2` é muito semelhante a
  `def f(x): return x * 2`, só que em linha e sem nome.
- Definida dentro de outra função, uma lambda **captura** as variáveis desse
  âmbito — `lambda x: x * n` captura `n` do local onde foi criada, por isso cada
  `multiplier(n)` produz uma função ligada ao seu próprio `n`.
- As lambdas servem para funções em linha *pequenas*, especialmente como o
  `key=` de `sorted` ou a função para `map`/`filter` (o resto deste capítulo).
  Para algo com várias instruções, usa um `def` com nome.

```python
double = lambda x: x * 2
double(5)                  # 10

def multiplier(n):
    return lambda x: x * n
multiplier(3)(4)           # 12
```
