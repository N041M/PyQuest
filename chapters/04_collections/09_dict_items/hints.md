Build the dict, then loop over d.items() to get each key and value.

---

`for k, v in d.items(): print(f"{k}={v}")`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
for k, v in d.items():
    print(f"{k}={v}")
