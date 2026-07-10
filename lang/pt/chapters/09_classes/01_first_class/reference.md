Uma **classe** define um novo tipo de objeto, juntando dados relacionados num
único valor. **`__init__`** é o inicializador: o Python chama-o
automaticamente quando crias uma instância, para preparar os seus dados
iniciais.

- `class Point:` abre a definição; chamar `Point(3, 4)` cria uma **instância**
  e executa `__init__`.
- **`self`** é a instância que está a ser construída; `self.x = x` guarda um
  valor como **atributo** nela, onde qualquer método o pode alcançar mais
  tarde.
- O primeiro parâmetro de `__init__` é sempre `self`; os restantes são os
  argumentos que quem chama passa.

```python
class Point:
    def __init__(self, x, y):
        self.x = x          # store data on the instance
        self.y = y

p = Point(3, 4)
p.x                         # 3
```
