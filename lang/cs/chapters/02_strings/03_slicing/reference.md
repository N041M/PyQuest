**Řez** `s[start:stop]` vrátí nový řetězec se znaky od pozice `start` **až po
`stop`, ten už ne** — *polootevřený* rozsah. Délka výsledku je `stop - start`
(když jsou oba v rozsahu).

- `s[2:5]` dá znaky na indexech 2, 3, 4 — tři znaky.
- Kteroukoli mez lze vynechat: `s[:3]` začíná od začátku, `s[3:]` běží do konce a
  `s[:]` zkopíruje celý řetězec.
- Řez nikdy nevyvolá chybu při mezích mimo rozsah — ořízne je. `s[:100]` u
  krátkého řetězce prostě vrátí celý.

```python
s = "Python"
s[0:3]    # 'Pyt'
s[:2]     # 'Py'
s[2:]     # 'thon'
```
