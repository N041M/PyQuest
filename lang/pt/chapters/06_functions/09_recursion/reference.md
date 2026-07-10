Uma função **recursiva** chama-se **a si própria** para resolver uma versão mais pequena do mesmo
problema. Duas partes são essenciais:

- um **caso base** que devolve diretamente **sem** recorrer — isto termina a
  recursão;
- um **caso recursivo** que chama a função sobre uma entrada mais pequena e constrói sobre
  o resultado, aproximando-se do caso base a cada vez.

Se o caso base falhar ou nunca for alcançado, as chamadas aninham-se até o Python levantar
`RecursionError`. Muitas recursões têm uma forma mais simples com ciclo; a recursão brilha quando
o problema é, em si, auto-semelhante.

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)   # smaller subproblem

factorial(4)   # 24
```
