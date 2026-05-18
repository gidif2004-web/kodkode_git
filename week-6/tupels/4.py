def reverse_tuple(tp):
    new_tp = ()
    for i in range(len(tp)-1,-1,-1):
        new_tp += (tp[i],)
    return new_tp
print(reverse_tuple((1,2,3,4,5,6)))