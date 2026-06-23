# 6.1 -- def: tvoje první funkce

## Koncept

**Funkce** je pojmenovaný, znovupoužitelný kus kódu. Funkce jsi *volal* celou dobu
-- `print()`, `len()`, `sorted()`. Teď si můžeš **definovat** vlastní:

```python
def double(x):
    return x * 2
```

- `def` zahajuje definici; `double` je jméno, které si zvolíš.
- `x` je **parametr**: proměnná, která přijme libovolnou hodnotu, jíž jí volající
  předá.
- `return` předá hodnotu **zpět volajícímu**. Volání `double(3)` je pak výraz s
  hodnotou `6`:

```python
result = double(3)     # result is 6
print(double(10))      # 20
```

**Tato kapitola kontroluje tvůj kód jinak.** Dosud se tvůj soubor *spouštěl* a
vypisoval. Odsud checker tvůj soubor **naimportuje** a **volá tvé funkce přímo** a
předává jim spoustu různých argumentů -- takže není potřeba žádný `input()` ani
`print()`. Tvůj soubor jen definuje funkci.

## Příklad

```python
def double(x):
    return x * 2
```

Celý tento soubor je platná odpověď na úlohu: definuje `double` a `double(21)`
vrátí `42`.

## Tvůj úkol

Definuj funkci `double(x)`, která **vrátí** `x` zdvojnásobené.

## Hotovo, když

- `double(3)` vrátí `6`, `double(0)` vrátí `0`, `double(-5)` vrátí `-10`.
- Tvůj soubor jen definuje funkci -- žádný `input()`, žádný `print()`.
