def get_adult_active_members(members_info):
    adult_active_members_names = []
    for member in members_info:
        name = member[0]
        age = member[1]
        is_adult = age >= 18
        is_active = member[2]
        if  is_adult and is_active:
            adult_active_members_names.append(name)
    return adult_active_members_names

members_info = [
    ["Dan", 25, True],
    ["Noa", 16, True],
    ["Yael", 30, False],
]

print(get_adult_active_members(members_info))