def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
