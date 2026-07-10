As cadeias de caracteres têm **métodos** — funções chamadas com a sintaxe `s.method()` que
calculam algo a partir da cadeia.

- **`.strip()`** devolve a cadeia com o **espaço em branco** inicial e final
  removido (espaços, tabulações, quebras de linha). `.lstrip()` / `.rstrip()` cortam apenas um lado.
- **`.upper()`** / **`.lower()`** devolvem a cadeia com todas as letras em maiúsculas
  ou minúsculas.

Como cada método devolve uma cadeia **nova** (a original nunca é modificada),
as chamadas **encadeiam-se**: cada uma atua sobre o resultado da anterior.

```python
"  Hi  ".strip()            # 'Hi'
"Hi".upper()                # 'HI'
"  Hello  ".strip().lower() # 'hello'  -- trimmed, then lowered
```
