Um **parâmetro** é um nome no cabeçalho da função que representa um valor que
quem chama fornece. Os valores passados numa chamada são os **argumentos**, associados aos
parâmetros da esquerda para a direita.

- `def f(a, b):` declara dois parâmetros; `f(3, 4)` chama com `a = 3`, `b = 4`.
- Os parâmetros são **locais**: só existem durante a chamada e não entram em conflito com
  nomes de fora. A função trabalha com o que quer que lhe seja dado, o que a torna reutilizável.
- Passar o número errado de argumentos levanta `TypeError`.

```python
def add(a, b):
    return a + b

add(3, 4)      # 7
```
