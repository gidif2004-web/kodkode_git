def swap_pairs(tp):
    new_tp = ()
    for i in range(0,len(tp),2):
        new_tp += tp[i+1], tp[i]
    return new_tp
print(swap_pairs((1,2,3,4,5)))