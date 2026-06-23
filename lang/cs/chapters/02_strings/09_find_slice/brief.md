# 2.9 -- Hledání pozice

## Koncept

`s.find(sub)` vrátí **index**, kde se `sub` poprvé objeví -- číslo, které pak můžeš
použít pro řez. (Pokud se `sub` nenajde, vrátí `-1`.)

```python
s = "name=Sam"
i = s.find("=")    # 4
print(i)           # 4
print(s[i+1:])     # Sam   (everything after the "=")
```

`find` tedy najde značku a řez vůči ní vytáhne část, kterou chceš. Zde `s[i+1:]`
znamená „od jedné pozice za `=` až do konce“.

## Příklad

```python
s = "color=blue"
i = s.find("=")
print(s[i+1:])     # blue
```

## Tvůj úkol

Každý vstup je řádek tvaru `key=value` (s jedním `=`). Vypiš jen **hodnotu** -- vše
za `=`.

Pro vstup `color=blue` je výstup:

```
blue
```

## Hotovo, když

- Pro `color=blue` vypíše `blue`.
- Pro `x=1` vypíše `1`; pro `a=` vypíše prázdný řádek; pro `k=a=b` vypíše `a=b`
  (rozdělí ho jen první `=`). Kontrola je zkouší.
