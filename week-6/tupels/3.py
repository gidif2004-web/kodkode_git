def count_occurrences(tp, val):
    counter = 0
    for value in tp:
        if value == val:
            counter += 1
    return counter
print (count_occurrences((1,2,1,21,2,1,2),2))