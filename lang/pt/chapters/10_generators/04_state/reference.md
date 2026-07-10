Um gerador **recorda** as suas variáveis locais entre `yield`s: a execução
congela no `yield` e cada variável local mantém o seu valor até que o
próximo pedido retome a função. Isto permite que um gerador **transporte
estado** enquanto transmite em fluxo.

- Uma variável atualizada no ciclo (um total acumulado, um valor anterior)
  persiste entre yields sem qualquer objeto ou variável global.
- É isto que faz de um gerador um **acumulador corrente** natural — uma soma
  acumulada, por exemplo, que emite o total até então a cada passo.

```python
def running_sum(nums):
    total = 0
    for n in nums:
        total += n          # total survives across yields
        yield total

list(running_sum([1, 2, 3]))    # [1, 3, 6]
```
