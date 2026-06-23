# 1.2 -- Vypisování více hodnot

## Koncept

Dvě nové myšlenky, obě o `print`.

**1. Více printů běží v pořadí.** Každý `print(...)` umístí svůj text na vlastní
řádek a Python je provádí shora dolů. Tři řádky s `print` vytvoří tři řádky
výstupu.

**2. Jeden print může zobrazit více hodnot.** Vlož do závorek několik věcí
oddělených **čárkami** a `print` je zobrazí na jednom řádku s jednou mezerou mezi
nimi:

```python
print("a", "b", "c")
```

zobrazí:

```
a b c
```

Takto můžeš míchat text a čísla. Čísla uvozovky **nepotřebují**; text ano.

## Příklad

```python
print("Scores:")
print(10, 20, 30)
```

zobrazí:

```
Scores:
10 20 30
```

První řádek je jeden print; druhý print má tři hodnoty oddělené čárkami, takže
sdílejí jeden řádek s mezerami mezi sebou.

## Tvůj úkol

Vytvoř přesně tyto dva řádky:

```
Counting:
1 2 3
```

Použij dva příkazy `print`: první vypíše slovo, druhý vypíše tři čísla `1`, `2`,
`3` jako samostatné hodnoty (mezery nech doplnit `print`).

## Hotovo, když

- Výstup jsou přesně dva řádky: `Counting:` a pak `1 2 3`.
- Druhý řádek vznikne z čísel oddělených čárkami, ne z toho, že sám napíšeš text
  `"1 2 3"`.
