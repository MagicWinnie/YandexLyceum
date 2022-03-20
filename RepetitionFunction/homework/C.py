def to_bytes(value, unit):
    if unit == "KB":
        return value * 2 ** 10
    elif unit == "MB":
        return value * 2 ** 10 * 2 ** 10
    elif unit == "GB":
        return value * 2 ** 10 * 2 ** 10 * 2 ** 10
    else:
        return value


def in_largest_units(value):
    if value // (2 ** 10) ** 3 != 0:
        return f"{round(value / (2**10)**3)} GB"
    elif value // (2 ** 10) ** 2 != 0:
        return f"{round(value / (2**10)**2)} MB"
    elif value // 2 ** 10 != 0:
        return f"{round(value / 2**10)} KB"
    else:
        return f"{value} B"
