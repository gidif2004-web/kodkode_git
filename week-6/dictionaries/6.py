def filter_by_value(d, threshold):
    keys_to_delete = []
    for key in d:
        if d[key] <= threshold:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del d[key]
    return d
