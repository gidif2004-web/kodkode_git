def key_with_maximum_value(d):
    maximum = None 
    for key in d:
        if not maximum or d[key] > d[maximum]:
            maximum = key
    return maximum
