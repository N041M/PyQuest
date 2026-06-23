Sestav slovník, pak projdi d.items(), abys získal každý klíč a hodnotu.

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
