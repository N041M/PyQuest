# 1.8 -- Aritmética e ordem

## Conceito

O Python faz contas com estes sinais (chamados **operadores**):

- `+` somar
- `-` subtrair
- `*` multiplicar
- `/` dividir

```python
print(2 + 3)   # 5
print(10 - 4)  # 6
print(6 * 7)   # 42
```

**A ordem importa.** Tal como na matemática da escola, `*` e `/` acontecem **antes**
de `+` e `-`. Portanto:

```python
print(2 + 3 * 4)   # 14, not 20  -- 3*4 first, then +2
```

Para forçar uma ordem diferente, envolve uma parte em **parênteses** `( )`. O que estiver
dentro dos parênteses é calculado primeiro:

```python
print((2 + 3) * 4)   # 20  -- 2+3 first, then *4
```

Esta é a fonte mais comum de erros de "número errado", por isso vale a pena
familiarizares-te com isto já.

## Exemplo

```python
print(1 + 2 * 3)     # 7
print((1 + 2) * 3)   # 9
```

## A tua tarefa

Imprime estas duas linhas:

```
14
20
```

- A primeira linha é `2 + 3 * 4` sem parênteses (multiplicação primeiro).
- A segunda linha usa os mesmos números mas com parênteses para que a soma
  aconteça primeiro: `(2 + 3) * 4`.

## Está feito quando

- O resultado é `14` depois `20`.
- A diferença entre as linhas vem apenas dos parênteses a mudar a
  ordem.
