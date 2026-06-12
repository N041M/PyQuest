while True around a try: convert-and-break; the except just goes around again.

---

except ValueError: pass  -- `pass` means "do nothing", which here means
"retry". Print AFTER the loop, where n is guaranteed good.

---

while True:
    try:
        n = int(input())
        break
    except ValueError:
        pass
print(n * 2)
