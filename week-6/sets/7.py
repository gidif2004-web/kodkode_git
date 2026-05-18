def first_repeated_element(lst):
    uniques = set()
    for val in lst:
        if val in uniques:
            return val
        uniques.add(val)
