def rotate_list(lst, k):
    counter = 0
    value = lst[0]
    index = 0
    flag = False
    k = k%len(lst)
    if len(lst)%2 == 0 and (k%2 == 0 or k == len(lst)//2):
        flag = True
        dubler = 2
        while True:
            if (k * dubler)%len(lst) == 0:
                break
            dubler += 1
        jump = dubler
    while counter != len(lst):
        if flag and counter != 0 and counter%jump == 0:
            index += 1
            index = index%len(lst)
            value = lst[index]
        index = index + k
        while index >= len(lst):
            index -= len(lst)
        lst[index], value = value, lst[index]
        counter += 1
    return lst
print (rotate_list([1,2,3,4,5,6,7,8,9,10],6))


