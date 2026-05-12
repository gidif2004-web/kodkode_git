highest = 0
while True:
    num = int(input('enter a number'))
    if num == 0:
        break
    if num > highest:
        highest = num
print(f'the highest number is {highest}')



