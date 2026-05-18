def group_by_first_letter(words):
    d = {}
    for word in words:
        d.setdefault(word[0], [])
        d[word[0]].append(word)
    return d
