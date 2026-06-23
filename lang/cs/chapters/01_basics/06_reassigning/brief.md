# 1.6 -- Přeřazení proměnné

## Koncept

Proměnnou lze po vytvoření **změnit**. Opětovné přiřazení témuž jménu nahradí
starou hodnotu novou. Jméno vždy odkazuje na to, co bylo uloženo **naposledy**.

```python
x = 10
print(x)   # 10
x = 20
print(x)   # 20
```

Na pořadí záleží: program běží shora dolů, takže první `print(x)` vidí `10` a `x`
se stane `20` až po druhém přiřazení.

Běžný a užitečný vzor je aktualizace proměnné pomocí její vlastní aktuální
hodnoty:

```python
x = 10
x = x + 5   # take the current x (10), add 5, store 15 back in x
print(x)    # 15
```

Nejprve se vyhodnotí pravá strana (`10 + 5`) a pak se výsledek uloží zpět do `x`.

## Častý omyl

Přeřazení nevytvoří druhou proměnnou. Stále existuje jen jedno `x`; jeho uložená
hodnota se vyměnila. Stará hodnota prostě zmizela.

## Tvůj úkol

Vytvoř proměnnou s hodnotou `10` a vypiš ji. Pak tutéž proměnnou přeřaď na `20` a
vypiš ji znovu. Výstup musí být:

```
10
20
```

## Hotovo, když

- Výstup je `10` a pak `20` na dvou řádcích.
- Oba řádky vypisují **stejnou** proměnnou, před změnou i po ní.
