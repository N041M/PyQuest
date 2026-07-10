Todo o valor tem um **tipo**. Dois tipos fundamentais aparecem logo de início:

- uma **cadeia de caracteres** (`str`) é texto, escrito entre aspas: `"42"`, `"hello"`;
- um **inteiro** (`int`) é um número, escrito como dígitos simples: `42`.

As aspas são toda a diferença. `type("42")` é `str`; `type(42)` é `int`.

O tipo decide o que um operador significa. `+` entre duas **cadeias de caracteres**
*concatena* (junta) -as; `+` entre dois **números** *soma*-os:

```python
"2" + "2"   # "22"  -- text joined
 2  +  2    #  4    -- numbers added
```

Misturar os dois com `+` é um erro (`TypeError`), porque o Python não vai adivinhar
se querias somar ou juntar. Converte explicitamente primeiro: `int("2") + 2` é
`4`, e `"$" + str(2)` é `"$2"`.
