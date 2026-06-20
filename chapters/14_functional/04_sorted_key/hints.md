`sorted(words, key=...)` sorts by whatever the key function returns. You want to
sort by the last character of each word.

---

The last character of `w` is `w[-1]`, so the key is `lambda w: w[-1]`:
`sorted(words, key=lambda w: w[-1])`.

---

def by_last(words):
    return sorted(words, key=lambda w: w[-1])
