def tuple_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
print(tuple_max((1,2,3,5,7,4,5)))