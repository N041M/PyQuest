# 2.5 -- Passos e inverter

## Conceito

Uma fatia pode levar um terceiro número, o **passo**: `s[start:stop:step]`. O passo indica
quantas posições avançar de cada vez. Um passo de `2` retira cada segundo caractere:

```python
s = "abcdef"
print(s[::2])   # ace   (every 2nd character)
```

Um passo **negativo** anda para trás. O atalho `s[::-1]` -- início vazio, fim
vazio, passo `-1` -- inverte a cadeia inteira:

```python
s = "python"
print(s[::-1])   # nohtyp
```

`s[::-1]` é a forma padrão em Python de inverter uma cadeia.

## Exemplo

```python
print("hello"[::-1])   # olleh
```

## A tua tarefa

Lê uma palavra e depois imprime-a **invertida**.

Para a entrada `hello` a saída é:

```
olleh
```

## Está feito quando

- Para `hello` imprime `olleh`.
- Para uma única letra, ou uma palavra que se lê igual ao contrário (como `level`), imprime
  a palavra sem alterações. O verificador testa ambos os casos.
