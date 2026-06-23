Nejprve přečti VŠECHNA jména do jednoho seznamu, pak všechna skóre do dalšího --
teprve potom je spáruj.

---

`for name, score in zip(names, scores):` dá jednu dvojici na průchod; vypiš obě s
mezerou mezi (to udělá prosté `print(name, score)`).

---

n = int(input())
names = []
for _ in range(n):
    names.append(input())
scores = []
for _ in range(n):
    scores.append(input())
for name, score in zip(names, scores):
    print(name, score)
