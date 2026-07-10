# 2.1 -- Indexação

## Conceito

Uma cadeia de caracteres é uma sequência de caracteres, e cada caractere tem uma **posição**
(chamada de *índice*). A contagem começa em **0**, não em 1. Assim, na cadeia `"cat"`:

```
character:  c  a  t
index:      0  1  2
```

Lês um único caractere com parênteses retos: `s[index]`.

```python
word = "cat"
print(word[0])   # c
print(word[1])   # a
```

`word[0]` é o primeiro caractere, porque a indexação começa em zero. Isto confunde
quase toda a gente à primeira: o "primeiro" caractere está no índice 0.

## Exemplo

```python
s = "python"
print(s[0])   # p
```

## A tua tarefa

Lê uma palavra com `input()`, depois imprime apenas o seu **primeiro** caractere.

Para a entrada `hello` a saída é:

```
h
```

## Está feito quando

- Para `hello` imprime `h`.
- Funciona para qualquer palavra, incluindo uma palavra de uma só letra (o
  verificador testa algumas).
