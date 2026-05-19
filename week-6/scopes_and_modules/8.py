def public_names(m):
    full_list = dir(m)
    list_without_underscore = list(filter(lambda name:name[0] != '_' , full_list))
    return list_without_underscore

