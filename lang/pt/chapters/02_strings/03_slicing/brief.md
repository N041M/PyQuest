# 2.3 -- Fatiamento

## Conceito

Uma **fatia** retira um intervalo de caracteres de uma só vez: `s[start:stop]`. Inclui o
caractere em `start` e vai **até, mas sem incluir**, `stop`. A isto chama-se
*semiaberto*: o índice de paragem não é incluído.

```python
s = "python"
print(s[0:3])   # pyt   (indexes 0, 1, 2 -- not 3)
print(s[2:5])   # tho   (indexes 2, 3, 4)
```

Se omitires `start`, começa em 0; se omitires `stop`, vai até ao fim:

```python
print(s[:3])    # pyt   (same as s[0:3])
print(s[3:])    # hon   (from index 3 to the end)
```

Como o `stop` não é incluído, `s[0:3]` dá-te exatamente **3** caracteres.

## Exemplo

```python
s = "rainbow"
print(s[0:4])   # rain
```

## A tua tarefa

Lê uma palavra e depois imprime os seus **primeiros três** caracteres.

Para a entrada `hello` a saída é:

```
hel
```

## Está feito quando

- Para `hello` imprime `hel`.
- Para uma palavra com menos de três letras, imprime a palavra inteira -- fatiar para lá
  do fim é seguro e não gera erro. O verificador testa `hi`.
