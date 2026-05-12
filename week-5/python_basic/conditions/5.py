x = int(input('enter x'))
y = int(input('enter y'))
if 10 <= x <= 50 and 20 <= y <= 80:
    if x == 10 or x == 50 or y == 20 or y == 80:
        print('On the edge')
    else:
        print('Inside the rectangle')
else:
    print('Outside the rectangle')
