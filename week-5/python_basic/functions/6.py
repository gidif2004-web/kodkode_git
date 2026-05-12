def count_digits(n):
    counter = 0
    while n:
        n //= 10
        counter += 1
    return counter

