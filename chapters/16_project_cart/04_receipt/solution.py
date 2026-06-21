def receipt(items):
    lines = ["%s: $%.2f" % (name, price) for name, price in items]
    total = sum(price for name, price in items)
    lines.append("TOTAL: $%.2f" % total)
    return "\n".join(lines)
