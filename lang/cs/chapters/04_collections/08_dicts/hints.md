Vytvoř prázdný slovník, pak ukládej každou dvojici jako d[word] = number.

---

`d = {}`, v cyklu čti slovo + číslo pomocí `d[word] = int(input())`, pak přečti
dotaz a `print(d[query])`.

---

n = int(input())
d = {}
for _ in range(n):
    word = input()
    d[word] = int(input())
query = input()
print(d[query])
