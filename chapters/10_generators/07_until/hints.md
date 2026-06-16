Loop over the numbers. As soon as you see a `0`, stop the whole generator;
otherwise yield the number.

---

`for n in nums:` -- first `if n == 0: return` (this ends the generator), then
`yield n` for everything before the zero.

---

def until_zero(nums):
    for n in nums:
        if n == 0:
            return
        yield n
