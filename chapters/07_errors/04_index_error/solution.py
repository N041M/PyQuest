def item_or(items, i, default):
    try:
        return items[i]
    except IndexError:
        return default
