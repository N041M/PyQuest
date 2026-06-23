`as e` jde rovnou do řádku except:  except ValueError as e:

---

Uvnitř bloku except prostě print(e) -- objekt se vypíše jako svá zpráva.

---

line = input()
try:
    print(int(line))
except ValueError as e:
    print(e)
