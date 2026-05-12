word = input('Enter a word: ')
flag = True
for letter in word:
    if  not letter.isdigit() and not letter.isalpha():
        flag = False
print (flag)    


