**N-tice** je uspořádaná, **neměnná** posloupnost psaná čárkami (často v
závorkách): `(3, 4)`, nebo jen `3, 4`. Jakmile je vytvořena, nelze ji změnit.

- **Rozbalování** přiřadí položky posloupnosti několika jménům najednou:
  `a, b = point`. Počet na obou stranách se musí shodovat.
- Tím je umožněno jednořádkové **prohození** `a, b = b, a`: pravá strana se
  nejprve sestaví do n-tice, pak se rozbalí, takže není potřeba žádná pomocná
  proměnná.
- N-tici použij pro pevnou skupinu souvisejících hodnot (souřadnice, záznam);
  seznam použij, když kolekce roste nebo se mění.

```python
point = (3, 4)
x, y = point        # x = 3, y = 4
a, b = b, a         # swap in one line
```
