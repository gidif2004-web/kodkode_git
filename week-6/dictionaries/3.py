def count_characters(word):
    d = {}
    for letter in word:
        d.setdefault(letter, 0)
        d[letter] += 1
    return d
print(count_characters('banana'))