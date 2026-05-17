def second_largest(numbers):
    maximum = max(numbers)
    second_max = None
    for number in numbers:
        if number < maximum:
            if not second_max or number > second_max:
                second_max = number
    return second_max
