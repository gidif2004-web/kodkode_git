def invert_dictionary(d):
    fliped_dict = {}
    for key, value in d.items():
        fliped_dict[value] = key
    return fliped_dict
