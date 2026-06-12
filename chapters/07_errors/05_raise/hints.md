Guard first, return after: if the age is negative, raise; otherwise it's fine
as-is.

---

The guard is two lines:  if age < 0:  then
raise ValueError("age cannot be negative").

---

def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
