Escreve `area` como um método normal que devolve `self.width * self.height`,
e depois coloca `@property` na linha imediatamente acima de `def area`.

---

Com `@property`, quem chama escreve `r.area` (sem parênteses) e o método
executa-se de cada vez, por isso reflete sempre a largura e a altura atuais.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
