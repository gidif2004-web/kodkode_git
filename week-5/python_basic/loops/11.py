num = int(input('Enter a positive integer'))
reversed_num = 0
while num:
    reversed_num *= 10
    digit = num % 10
    num = num // 10
    reversed_num += digit
print(f'here is the reversed number: {reversed_num}')