def merge_sorted_lists(lst1, lst2):
    index1 = 0
    index2 = 0
    merged_list = []
    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] < lst2[index2]:
            merged_list.append(lst1[index1])
            index1 += 1
        else:
            merged_list.append(lst2[index2])
            index2 += 1
    merged_list.extend(lst1[index1:] + lst2[index2:])
    return merged_list
