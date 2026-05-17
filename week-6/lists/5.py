def remove_duplicates(lst):
    new_lst = []
    for val in lst:
        if val not in new_lst:
            new_lst.append(val)
    return new_lst
