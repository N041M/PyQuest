# 16.3 -- Ladění: sleva je špatně

## Krok 3 -- oprav chybu

Tentokrát je kód **už napsaný** -- a má chybu. `Cart` s metodou
`discounted_total(percent)` má z celku strhnout `percent` **procent**. Zákazníci ale
hlásí, že sleva je nehorázně příliš velká: 10% kupón na košík za \$50 účtuje \$40
místo \$45.

Otevři pracovní soubor, přečti `discounted_total`, zjisti, co vlastně dělá, a oprav
to. Zbytek třídy nech být.

## Hotovo, když

- `discounted_total(0)` se rovná plnému `total()` (žádná sleva).
- 10% sleva na košík za \$50 dá `45.0`, ne `40.0`.
- Pro libovolný celek `t` a procento `p` je `discounted_total(p)` rovno
  `t * (1 - p/100)`.
