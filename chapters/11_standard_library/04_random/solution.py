import random


def shuffled(items, seed):
    out = list(items)
    random.seed(seed)
    random.shuffle(out)
    return out
