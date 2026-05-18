def symmetric_difference(lst1, lst2):
    merged = []
    for item in lst1:
        if item not in lst2:
            merged.append(item)
    for item in lst2:
        if item not in lst1:
            merged.append(item)
    return merged
