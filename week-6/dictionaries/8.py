def word_frequency(text):
    words = text.split(' ')
    d = {}
    for word in words:
        d.setdefault(word, 0)
        d[word] += 1
    return d
