def zeros_to_the_end(arr):
    counter = 0
    for num in arr:
        if num != 0:
            arr[counter] = num
            counter += 1
    for i in range(len(arr) - counter):
        arr[counter + i] = 0
    return arr
