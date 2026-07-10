# 7.6 -- Pergunta outra vez: o ciclo de repetição

## Conceito

O uso clássico de `try`/`except` num programa a sério: **continuar a
perguntar até a entrada fazer sentido.** Combina um ciclo `while True` (3.7),
`break` (3.11), e o `except` de 7.1:

```python
while True:
    try:
        n = int(input())
        break              # got a good one -- leave the loop
    except ValueError:
        pass               # bad line -- silently go around again
```

A forma a interiorizar:

- o **caminho feliz** termina em `break`;
- o **except** absorve a falha e deixa o ciclo tentar outra vez;
- depois do ciclo, `n` está garantidamente válido -- o código a seguir pode
  confiar nele.

(`pass` é a instrução do Python para "não fazer nada" -- o bloco except tem
de conter *alguma coisa*.)

## Exemplo

Para as linhas de entrada `cat`, `dog`, `21` o programa ignora as duas
primeiras e imprime `42`.

## A tua tarefa

Lê linhas até uma se converter num número inteiro, depois imprime esse
número **duplicado**. Linhas inválidas não produzem qualquer saída.

## Está feito quando

- `21` como primeira linha imprime `42`.
- `cat`, `dog`, `21` também imprime apenas `42` -- o lixo é repetido em
  silêncio.
- Números negativos funcionam.
- Usaste um ciclo e `try`/`except`.
