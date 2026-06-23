`__init__` je obyčejná funkce, takže její parametry mohou mít **výchozí hodnoty** —
což umožní objekt vytvořit s určitými argumenty i bez nich.

- `def __init__(self, balance=0):` dovolí `Account()` (začne na 0) nebo
  `Account(100)` (začne na 100).
- Platí stejná pravidla: parametry s výchozí hodnotou jdou za těmi bez ní a
  měnitelná výchozí hodnota potřebuje trik se sentinelem `None`
  (`def __init__(self, items=None): self.items = items or []`).
- Výchozí hodnoty dělají běžný případ bez námahy a zároveň drží možnost otevřenou.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance

Account().balance        # 0
Account(100).balance     # 100
```
