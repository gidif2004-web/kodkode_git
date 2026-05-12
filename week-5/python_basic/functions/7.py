def reverse_int(n):
    n_str = str(n)
    while n_str[-1] == '0':
        n_str = n_str[:-1]
    n_str = n_str[::-1]
    if n_str[-1] == '-':
        n_str = '-' + n_str[:-1]
    return n_str
print(reverse_int(-765400))
