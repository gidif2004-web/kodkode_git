age = int(input())
if 120 > age > 0:
    if age <= 12:
        print('Child')
    elif age <= 17:
        print('Teen')
    else:
        print('Adult')
else:
    print('invalid') 