def count_occurrences(lst, val):
    #return lst.count(val)
    counter = 0
    for value in lst:
        if value == val:
            counter += 1 
    return counter
