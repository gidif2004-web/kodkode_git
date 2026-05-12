age = int(input('your age: '))
vip = input('do you heve a vio card? (y/n)')
if age >= 18:
    if 21 >= age <= 19 or vip == 'y':
        print('please enter')
    else:
        print('you cant enter')
else:    
    print('you cant enter')
