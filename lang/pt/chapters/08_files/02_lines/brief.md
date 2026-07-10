# 8.2 -- Um ficheiro, linha a linha

## Conceito

`f.read()` dá-te tudo de uma vez. Mais frequentemente queres o ficheiro **uma
linha de cada vez** -- e um objeto de ficheiro é *iterável*, por isso um ciclo
`for` percorre as suas linhas por ti:

```python
with open("tasks.txt") as f:
    for line in f:
        ...
```

Um pormenor: cada `line` ainda traz a quebra de linha que a terminou --
`"wash\n"`, não `"wash"`. Remove-a com `line.strip()` (3.7) antes de usares o
texto, ou a tua saída acumula linhas em branco.

## Exemplo

Para um `tasks.txt` de:

```
wash
cook
sleep
```

numerar cada linha dá:

```
1. wash
2. cook
3. sleep
```

`enumerate` (5.5) é a escolha natural -- começa-o em `1`:

```python
for i, line in enumerate(f, start=1):
    print(f"{i}. {line.strip()}")
```

## A tua tarefa

Lê `tasks.txt` e imprime cada linha **numerada a partir de 1**, na forma
`1. wash`. Remove a quebra de linha final para não haver linhas em branco
soltas.

## Está feito quando

- Cada linha é impressa como `<número>. <texto>`, contando a partir de 1.
- Funciona para um ficheiro de qualquer comprimento.
- Abriste o ficheiro com `with` e percorreste-o com `for`.
