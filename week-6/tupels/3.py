def count_occurrences(tp, val):
    counter = 0
    for value in tp:
        if value == val:
            counter += 1
    return counter
