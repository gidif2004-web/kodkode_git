def distindt_word(text):
    words = text.lower().split(' ')
    return len(set(words))
