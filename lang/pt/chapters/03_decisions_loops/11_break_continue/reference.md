Duas instruções alteram o fluxo de um ciclo a partir de dentro dele:

- **`break`** termina o ciclo **imediatamente**, saltando quaisquer passagens
  restantes e avançando para o código depois do ciclo. Usa-o para parar assim que
  encontrares o que procuravas.
- **`continue`** salta o **resto da passagem atual** e avança diretamente para a
  iteração seguinte do ciclo (voltando a verificar a condição / passando para o
  item seguinte).

Ambos afetam apenas o ciclo **mais interior** que os envolve.

```python
for n in range(10):
    if n == 5:
        break             # stop the whole loop at 5
    if n % 2 == 0:
        continue          # skip evens, go to the next n
    print(n)              # 1, 3
```
