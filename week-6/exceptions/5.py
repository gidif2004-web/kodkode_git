def set_age(age):
    if age < 0 or age > 150:
        raise ValueError
    else:
        return age
