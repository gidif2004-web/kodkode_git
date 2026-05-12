def no_duplicates(arr):
    help_arr = []
    for value in arr:
        if value not in help_arr:
            help_arr.append(value)
    return help_arr
