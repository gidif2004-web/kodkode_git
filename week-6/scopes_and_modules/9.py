# this is the problem the defult value evaluate only once

def add_item(item, bag=[]):
    bag.append(item)
    return bag

print(add_item(3)) # output: [3]
print(add_item(2)) # output: [3, 2]
print(add_item(1)) # output: [3, 2, 1]

# the correct way:

def add_item_correct(item, bag = None):
    if not bag:
        bag = []
    bag.append(item)
    return bag

print(add_item_correct(3)) # output: [3]
print(add_item_correct(2)) # output: [2]
print(add_item_correct(1)) # output: [1]