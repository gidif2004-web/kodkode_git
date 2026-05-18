def elements_in_only_one(lst1, lst2):
    return list(sorted(set(lst1)^set(lst2)))
