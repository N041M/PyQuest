A **character class** `[...]` matches **exactly one** character from the set
listed inside it. `[aeiou]` matches any single vowel; `[abc]` matches `a`, `b`,
or `c`.

- A **range** with a hyphen covers consecutive characters: `[a-z]` any lowercase
  letter, `[0-9]` any digit, `[A-Za-z0-9]` any letter or digit. Combine sets and
  ranges freely inside one class.
- A leading **`^`** negates: `[^aeiou]` matches any character that is *not* a
  vowel.
- The class matches **one** character; add a quantifier for a run — `[a-z]+` is a
  word, `[0-9]{4}` exactly four digits. Inside a class most metacharacters lose
  their special meaning (`[.]` is a literal dot).

```python
import re

re.findall(r"[aeiou]", "education")   # ['e', 'u', 'a', 'i', 'o']
re.findall(r"[^a-z ]", "a1 b2!")      # ['1', '2', '!']
re.findall(r"[A-Z][a-z]+", "Ada Lovelace")   # ['Ada', 'Lovelace']
```
