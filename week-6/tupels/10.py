def rotate_tuple(tp, k):
    lst = list(tp)
    for i in range(k % len(tp)):
        val = lst.pop()
        lst.insert(0, val)
    return tuple(lst)
