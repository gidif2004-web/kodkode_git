def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

def digital_root(n):
    while n > 9:
        n = sum_digits(n)
    return n
