def parse_ints(values):
    for i, value in enumerate(values):
        try:
            values[i] = int(value)
        except:
            values.pop(i)
    return values
