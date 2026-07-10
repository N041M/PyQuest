Um ciclo com **sentinela** lê valores repetidamente e para quando encontra um valor
especial de "paragem", em vez de o fazer após uma contagem fixa. O padrão é um `while`
cuja condição testa a entrada mais recente contra a sentinela.

- Lê uma vez antes do ciclo (ou lê no início de cada passagem), e depois compara com
  a sentinela para decidir se continuas.
- A própria sentinela **não** é processada — a verificação acontece antes do trabalho,
  pelo que o valor de paragem termina o ciclo em vez de ser contado.

```python
line = input()
while line != "quit":     # "quit" is the sentinel
    print("you said:", line)
    line = input()        # read the next, then re-check
```
