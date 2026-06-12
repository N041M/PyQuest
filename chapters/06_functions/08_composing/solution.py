def clean(text):
    return text.strip().lower()


def same_word(a, b):
    return clean(a) == clean(b)
