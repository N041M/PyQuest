# 1.4 -- Comentários

## Conceito

Um **comentário** é uma nota no teu código que o Python ignora. Tudo o que vier depois de um `#` numa
linha é ignorado quando o programa corre. Os comentários são para humanos -- para explicar
o que o código faz.

```python
# This whole line is a note and does nothing.
print("Hi")   # Text after # on a code line is also ignored.
```

Só `print("Hi")` corre acima. As duas notas são ignoradas.

Um segundo uso, muito prático: **comentar** código. Se colocares um `#` à frente
de uma linha de código real, essa linha deixa de correr -- sem a apagares. É assim
que desligas uma linha temporariamente.

```python
# print("off")
print("on")
```

Só `on` é impresso; a primeira linha é agora um comentário.

## Erro comum

Colocar `#` à frente de uma linha **não** a apaga nem causa um erro -- a
linha simplesmente não corre. Remove o `#` e ela volta a correr.

## A tua tarefa

O ficheiro inicial já contém uma linha que imprime `Hidden`. **Comenta-a**
para que não corra -- **não** a apagues -- e acrescenta uma linha que imprima
`Visible`.

O programa tem de imprimir apenas:

```
Visible
```

## Está feito quando

- O resultado é exatamente `Visible`.
- A linha `print("Hidden")` continua no ficheiro, mas comentada com um `#`
  para que não corra. (Este puzzle é sobre *comentar código*, por isso apagar a
  linha não conta.)
