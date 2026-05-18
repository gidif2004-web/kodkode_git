def common_keys(d1, d2):
    muteral_keys = []
    for key in d1:
        if key in d2:
            muteral_keys.append(key)
    muteral_keys.sort()
    return muteral_keys
