**`raise`** spustí výjimku **ty sám**, zastaví funkci a signalizuje, že je něco
špatně. Umožní tvému kódu odmítnout špatný vstup v bodě, kde je zjištěn, stejně
jako to dělají vestavěné funkce.

- `raise ValueError("amount must be positive")` sestaví výjimku se zprávou a vyhodí
  ji; běh se zastaví, pokud ji nezachytí nějaký `try` výše v řetězci volání.
- Zvol typ, který sedí: `ValueError` pro špatnou hodnotu, `TypeError` pro špatný
  typ. Zpráva vysvětlí, co se očekávalo.
- Vyvolání chyby na hranici (jak vstup přichází) udrží zbytek kódu schopným
  důvěřovat svým datům.

```python
def withdraw(amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    ...
```
