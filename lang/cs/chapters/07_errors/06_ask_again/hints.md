while True kolem try: převeď-a-break; except prostě jde znovu dokola.

---

except ValueError: pass  -- `pass` znamená „nedělej nic“, což tady znamená
„zkus znovu“. Vypiš AŽ PO cyklu, kde je n zaručeně dobré.

---

while True:
    try:
        n = int(input())
        break
    except ValueError:
        pass
print(n * 2)
