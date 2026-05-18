def min_and_max(tp):
    minimum = maximum = tp[0]
    for val in tp:
        if val > maximum:
            maximum = val
        if val < minimum:
            minimum = val
    return minimum, maximum
