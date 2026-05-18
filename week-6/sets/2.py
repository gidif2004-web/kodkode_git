def count_unique_elements(lst):
    uniques = set(lst)
    counter = 0
    for val in uniques:
        counter += 1
    return counter
