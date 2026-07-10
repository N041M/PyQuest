# 7.8 -- Capstone: uma calculadora robusta

## Conceito

Um único `try` pode ter **vários** blocos `except` -- um por cada tipo de
falha, cada um escolhendo a sua própria recuperação:

```python
try:
    ...
except ValueError:
    print("bad number")
except ZeroDivisionError:
    print("cannot divide")
```

Seja qual for o erro levantado, este escolhe o seu bloco correspondente; os
outros são ignorados. Este capstone liga todo o capítulo ao exercício
clássico: uma calculadora que **não pode ser feita cair** pela sua entrada.
Também precisa de `split` (4.4), indexação (2.1), `elif` (3.4), e `/` (1.9).

## Exemplo

```
input "8 + 5"   ->  13
input "9 / 2"   ->  4.5
input "9 / 0"   ->  cannot divide
input "two * 3" ->  bad number
input "8 ? 5"   ->  unknown op
```

## A tua tarefa

Lê uma linha da forma `<number> <op> <number>` (três partes separadas por
espaços). Para as operações `+`, `-`, `*` imprime o resultado como número
inteiro; para `/` imprime o resultado como float. Trata todas as falhas:

- uma parte que não é um número inteiro -> imprime `bad number`
- divisão por zero -> imprime `cannot divide`
- qualquer outro símbolo de operação -> imprime `unknown op`

## Está feito quando

- `8 + 5` -> `13`, `9 / 2` -> `4.5`, `3 * -2` -> `-6`.
- `9 / 0` -> `cannot divide`; `two * 3` -> `bad number`; `8 ? 5` ->
  `unknown op`.
- Nenhuma entrada o faz cair: cada falha imprime a sua própria mensagem
  através de blocos `except` (e um `else`/`elif` para a operação
  desconhecida).
