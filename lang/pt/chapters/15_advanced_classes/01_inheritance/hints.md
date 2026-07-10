Escreve primeiro `Animal`, com `__init__` a guardar `self.name` e `describe`
a devolver a frase. Depois `class Dog(Animal):` -- é o `(Animal)` que faz Dog
herdar.

---

Dentro de `Dog` só escreves `speak`; `describe` vem de graça de `Animal`.
Não redefinas `describe` em `Dog`.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return self.name + " the animal"


class Dog(Animal):
    def speak(self):
        return "Woof"
