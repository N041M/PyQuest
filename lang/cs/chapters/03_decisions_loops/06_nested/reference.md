Blok `if` může sám obsahovat další `if` — **vnořování**. Vnitřní test proběhne
**jen když** byla vnější podmínka pravdivá, takže vnořování vyjadřuje „tohle, a pak
uvnitř toho tohle“.

- Každá úroveň přidá krok odsazení; vnitřní blok je odsazený pod vnitřní `if`.
- Vnořování a `and` mohou vyjádřit totéž — `if a: if b:` je jako `if a and b:` —
  ale vnořování je správný nástroj, když vnější případ potřebuje vlastní ošetření
  (např. `else`) oddělené od vnitřního.
- Drž vnoření mělké; hluboké pyramidy se špatně čtou a řetěz `elif` nebo časný
  `return` se často čte lépe.

```python
if logged_in:
    if is_admin:
        show_admin_panel()   # only when logged_in AND is_admin
    else:
        show_user_panel()    # logged_in but not admin
```
