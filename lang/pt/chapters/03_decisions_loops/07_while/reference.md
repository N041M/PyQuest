Um ciclo **`while`** repete o seu bloco **enquanto** a sua condição se mantiver verdadeira.
A condição é verificada **antes** de cada passagem; quando se torna falsa, o ciclo
termina e o programa continua abaixo.

- Algo dentro do ciclo tem de acabar por tornar a condição falsa (por exemplo, avançar
  um contador), ou então o ciclo repete-se para sempre — um ciclo infinito.
- Se a condição for falsa logo na primeira verificação, o corpo executa-se zero vezes.
- Usa `while` quando não sabes de antemão o número de passagens (fazes o ciclo até
  algo acontecer); usa `for` quando estás a contar um intervalo conhecido.

```python
n = 3
while n > 0:
    print(n)
    n = n - 1        # moves toward ending the loop -> 3, 2, 1
```
