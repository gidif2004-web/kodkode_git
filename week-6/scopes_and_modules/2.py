def make_counter():
    counter = 0
    def bump():
        nonlocal counter
        counter += 1
        return counter
    return bump
