# 1.7 -- Texto vs número

## Conceito

O Python distingue dois tipos de valores, e isso importa muito:

- Um **número** como `5` -- escrito sem aspas. O Python chama aos números inteiros
  `int` (integer).
- Uma **cadeia de caracteres** como `"5"` -- escrita entre aspas. É *texto* que por acaso
  se parece com um número. O Python chama-lhe `str`.

Comportam-se de forma diferente com o sinal `+`:

- Com números, `+` **soma**: `5 + 5` é `10`.
- Com cadeias de caracteres, `+` **junta** (a isto chama-se **concatenação**):
  `"5" + "5"` é `"55"` -- os dois pedaços de texto colados um ao outro.

```python
print(5 + 5)        # 10   (numbers add)
print("5" + "5")    # 55   (text joins)
print("ab" + "cd")  # abcd
```

Portanto `"5"` e `5` parecem iguais no ecrã mas são tipos diferentes, e `+` trata-os
de formas completamente diferentes.

## Erro comum

`"5"` não é o número cinco. As aspas fazem dele texto. Não podes fazer aritmética
com ele à espera de uma soma -- `"5" + "5"` dá `"55"`, não `10`.

## A tua tarefa

Imprime estas duas linhas, por esta ordem:

```
55
10
```

- A primeira linha tem de vir de **juntar duas cadeias de caracteres** `"5"` e `"5"` com `+`.
- A segunda linha tem de vir de **somar dois números** `5` e `5` com `+`.

## Está feito quando

- O resultado é `55` depois `10`.
- A primeira linha usa concatenação de texto; a segunda usa soma de números.
