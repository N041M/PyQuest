# 2.7 -- Čištění textu

## Koncept

Řetězce mají **metody** -- akce, které voláš s tečkou za řetězcem: `s.metoda()`.
Tři běžné:

- `s.upper()` -> kopie VELKÝMI písmeny
- `s.lower()` -> kopie malými písmeny
- `s.strip()` -> kopie s mezerami odstraněnými z **obou konců** (ne z prostředku)

```python
"Hello".upper()     # "HELLO"
"Hello".lower()     # "hello"
"  hi  ".strip()    # "hi"
```

Metody vracejí **nový** řetězec; originál nemění. Můžeš je řetězit -- každá pracuje
na výsledku té předchozí:

```python
"  Hi  ".strip().upper()   # "HI"
```

## Příklad

```python
s = "  python  "
print(s.strip().upper())   # PYTHON
```

## Tvůj úkol

Přečti řádek, odstraň kolem něj mezery a vypiš ho **velkými písmeny**.

Pro vstup `  hello  ` je výstup:

```
HELLO
```

## Hotovo, když

- Pro `  hello  ` vypíše `HELLO`.
- Mezery uprostřed zůstanou; oříznou se jen konce. Kontrola zkouší i řádek tvořený
  jen mezerami (výsledkem je prázdný řádek).
