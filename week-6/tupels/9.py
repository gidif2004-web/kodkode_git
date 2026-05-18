def frequency_table(tp):
    final_tp = ()
    checked_list = []
    for item in tp:
        if item not in checked_list:
            counter = 0
            for inner_item in tp:
                if item == inner_item:
                    counter += 1
            final_tp += ((item, counter),)
            checked_list += item
    return final_tp
print(frequency_table(('a', 'b', 'a', 'c', 'b', 'a')))