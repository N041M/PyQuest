# 9.6 -- Rozumná výchozí hodnota

## Koncept

Konstruktor je jen funkce, takže může brát i **výchozí parametry** (6.4). To
umožní volajícímu vynechat to, co ho nezajímá, a přesto dostat funkční objekt.

```python
class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def greet(self, name):
        return f"{self.greeting}, {name}!"
```

Pokud pozdrav nepředáš, dostaneš `"Hello"`; pokud ano, použije se místo toho:

```python
Greeter().greet("Ada")        # "Hello, Ada!"
Greeter("Hi").greet("Bo")     # "Hi, Bo!"
```

Výchozí hodnota žije v signatuře `__init__` (`greeting="Hello"`), takže objekt se
nakonfiguruje jednou při stavbě a každý `greet` ji znovu použije.

## Tvůj úkol

Definuj třídu `Greeter`, jejíž `__init__` bere `greeting`, který **má výchozí
hodnotu `"Hello"`**, a uloží ho. Přidej metodu `greet(name)`, která vrátí
`"{greeting}, {name}!"`.

## Hotovo, když

- `Greeter().greet("Ada")` je `"Hello, Ada!"` (použita výchozí hodnota).
- `Greeter("Hi").greet("Bo")` je `"Hi, Bo!"` (výchozí hodnota přepsána).
- Výchozí hodnota je výchozí *parametr* `__init__`, ne `if` uvnitř něj.
