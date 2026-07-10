Um objeto guarda **estado** — dados que persistem entre chamadas. Um método
pode **alterar** `self`, e a chamada seguinte ao método vê a mudança, por isso
o objeto lembra-se do que lhe aconteceu.

- `self.count += 1` atualiza um atributo no próprio lugar; o novo valor
  mantém-se até ser alterado de novo.
- É esse o objetivo dos objetos: transportam os seus dados consigo entre
  chamadas, ao contrário de uma função simples cujas variáveis locais
  desaparecem quando ela termina.
- Cada instância tem a sua **própria** cópia dos atributos, por isso dois
  contadores contam de forma independente.

```python
class Counter:
    def __init__(self):
        self.n = 0
    def tick(self):
        self.n += 1         # remembered for next time

c = Counter(); c.tick(); c.tick(); c.n   # 2
```
