A **library** here means a set of related functions you've written, each named
for its job, that together form a reusable toolkit — the payoff of the chapter.

- Build small functions that each do one thing and `return` their result; then
  higher-level functions call them. Calling code reads as a sequence of intents.
- Keeping logic inside named functions (rather than copied inline) means a fix or
  improvement lands in one place and every caller benefits.

```python
def clean(s):    return s.strip().lower()
def words(s):    return clean(s).split()
def wordcount(s): return len(words(s))

wordcount("  The quick fox ")   # 3  -- each function builds on the last
```
