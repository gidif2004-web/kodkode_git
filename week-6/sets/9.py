def pair_sum_exists(lst, target):
    uniques = set(lst)
    for num in lst:
        if target-num != num and target-num in uniques:
            return True
    return False
