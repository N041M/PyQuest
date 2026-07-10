# 6.10 -- Capítulo final: uma pequena biblioteca

## Conceito

Nada de novo -- este capítulo final é o capítulo em miniatura: várias funções,
cada uma com um trabalho claro, as últimas a **delegar** nas anteriores
(6.8). Um ficheiro de funções relacionadas como este é a semente de qualquer
*biblioteca* real que alguma vez vieres a importar.

As peças: `for ch in word` (3.10), `in` (5.1), a ideia da contagem (5.9),
f-strings (2.10), e retornos antecipados (6.5).

## Exemplo

```python
count_vowels("tea")        # 2   ("e" and "a")
count_vowels("xyz")        # 0
describe("tea")            # "tea has 2 vowels"
describe("xyz")            # "xyz has no vowels"
```

## A tua tarefa

Define **ambas** as funções:

- `count_vowels(word)` -- devolve quantos caracteres de `word` são vogais
  (`a`, `e`, `i`, `o`, `u`; as palavras estão em minúsculas).
- `describe(word)` -- devolve a string `"<word> has <n> vowels"`, exceto
  quando a contagem é zero: nesse caso é `"<word> has no vowels"`. Tem de **chamar
  `count_vowels`**.

## Está feito quando

- `count_vowels("tea")` é `2`; `count_vowels("xyz")` é `0`.
- `describe("tea")` é `"tea has 2 vowels"`; `describe("xyz")` é
  `"xyz has no vowels"`.
- `describe` delega em `count_vowels` -- o verificador procura a chamada.
