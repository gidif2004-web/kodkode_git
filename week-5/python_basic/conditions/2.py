letter = input()
if 'z' >= letter >= 'a' or 'Z' >= letter >= 'A': 
    if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        print('Vowel')
    else: 
        print('Consonant')
else:
    print('Invalid')