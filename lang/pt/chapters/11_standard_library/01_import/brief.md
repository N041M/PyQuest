# 11.1 -- import: trazer um módulo

## Conceito

O Python vem com uma grande **biblioteca padrão**: ferramentas prontas agrupadas em
**módulos**. Não os tens de graça em cada ficheiro -- **importas**
o módulo de que precisas e depois acedes ao seu conteúdo através do seu nome.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
```

- `import math` executa-se uma vez no topo do ficheiro e associa o nome `math` a
  todo o módulo.
- A partir daí, `math.sqrt` é a função de raiz quadrada e `math.pi` a
  constante -- `module.name` acede a tudo o que o módulo disponibiliza.

A vantagem de importar é que alguém já escreveu e testou isto, por isso
chamas `math.sqrt` em vez de deduzires tu próprio uma raiz quadrada.

## Exemplo

```python
import math

def diagonal(side):
    return math.sqrt(2) * side
```

## A tua tarefa

Define `hypotenuse(a, b)` que devolve o comprimento da hipotenusa de um
triângulo retângulo com catetos `a` e `b` -- a raiz quadrada de `a*a + b*b` --
usando **`math.sqrt`** do módulo `math` importado.

## Está feito quando

- `hypotenuse(3, 4)` devolve `5.0`, `hypotenuse(5, 12)` devolve `13.0`.
- `hypotenuse(0, 0)` devolve `0.0`.
- A raiz quadrada vem de `math.sqrt`, através de `import math`.
