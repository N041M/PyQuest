The `as e` goes right in the except line:  except ValueError as e:

---

Inside the except block, just print(e) -- the object prints as its message.

---

line = input()
try:
    print(int(line))
except ValueError as e:
    print(e)
