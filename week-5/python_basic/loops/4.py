vowels = ['a' ,'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
counter  = 0
word = input('enter a word')
for letter in word:
    if letter in vowels:
        counter += 1
print(f'the number of vowels in the word is: {counter}')