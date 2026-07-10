# 1.5 -- Guardar um valor

## Conceito

Uma **variável** é um nome que guarda um valor para poderes usá-lo mais tarde. Crias
uma com `=`, o sinal de **atribuição**:

```python
score = 100
```

Lê isto como "seja `score` igual a `100`." O nome fica do lado esquerdo, o valor do lado
direito. Depois dessa linha, escrever `score` em qualquer lado significa `100`.

Isto é diferente de `==` (que vais encontrar mais tarde para comparar). Um único
`=` *guarda*.

Uma vez guardado, podes usar o nome tantas vezes quantas quiseres:

```python
score = 100
print(score)
print(score)
```

mostra:

```
100
100
```

Repara que `print(score)` **não tem aspas** à volta de `score`. Aspas fariam disso o
texto literal "score"; sem aspas significa o valor da variável, `100`.

## Regras de nomeação (versão rápida)

Um nome de variável pode usar letras, dígitos e sublinhados, mas não pode começar com um
dígito nem conter espaços. Usa nomes claros: `total`, `user_name`, `count`.

## A tua tarefa

Guarda o número `42` numa variável, depois imprime essa variável **duas vezes** para que o
resultado seja:

```
42
42
```

Usa a variável nas duas vezes -- não escrevas `42` dentro dos prints.

## Está feito quando

- O resultado é `42` em duas linhas separadas.
- Ambas as linhas vêm de imprimir a tua variável (sem aspas à volta do seu nome).
