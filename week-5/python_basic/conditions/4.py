password = 'l'
user_password = input('Enter password: ')
if password == user_password:
    print('Access Granted')
elif len(user_password) < 8:
    print('Too short')
else:
    print('Wrong password')
    