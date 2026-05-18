def rotate_tuple(tp, k):
    lst = list(tp)
    for i in range(k % len(tp)):
        val = lst.pop()
        lst.insert(0, val)
    return tuple(lst)
print(rotate_tuple((1,2,3,4,5,6),7))