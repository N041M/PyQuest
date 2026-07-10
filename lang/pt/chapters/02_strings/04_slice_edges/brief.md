# 2.4 -- Fatiar o meio

## Conceito

O fatiamento combina-se bem com índices negativos, e as fatias nunca rebentam -- se uma fatia
está vazia, obténs simplesmente a cadeia vazia `""`.

`s[1:-1]` significa "do índice 1 até (mas sem incluir) o último caractere" -- por
outras palavras, elimina o primeiro e o último caracteres:

```python
s = "python"
print(s[1:-1])   # ytho
```

Se a cadeia for demasiado curta para ter um meio, a fatia é simplesmente vazia:

```python
print("ab"[1:-1])   # (nothing -- an empty string)
print("a"[1:-1])    # (nothing)
```

Sem erro. Uma fatia vazia é um resultado normal e válido.

## Erro comum

Ir "fora do intervalo" com uma fatia **não** provoca erro, ao contrário de indexar um único
caractere. `"hi"[5]` seria um erro, mas `"hi"[1:5]` está bem -- simplesmente para
no fim.

## Exemplo

```python
s = "hello"
print(s[1:-1])   # ell
```

## A tua tarefa

Lê uma palavra e depois imprime-a **sem o primeiro e o último caracteres**.

Para a entrada `hello` a saída é:

```
ell
```

## Está feito quando

- Para `hello` imprime `ell`.
- Para uma palavra de 1 ou 2 letras imprime uma linha vazia (sem meio) e não
  rebenta. O verificador testa `ab` e `a`.
