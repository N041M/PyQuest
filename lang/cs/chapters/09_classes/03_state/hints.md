`__init__` nastaví výchozí bod: `self.count = 0`. Pak `tick` ho mění.

---

Uvnitř `tick` udělej `self.count = self.count + 1` (nebo `self.count += 1`), pak
`return self.count`. Drž počet na `self`, aby každý čítač měl svůj vlastní.

---

class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1
        return self.count
