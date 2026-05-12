num = int(input('Enter a positive integer'))
counter = 0
while num:
    digit = num % 10
    num = num // 10
    if digit % 2 == 0:
        counter += 1
print (f'there is {counter} even digits in the number')