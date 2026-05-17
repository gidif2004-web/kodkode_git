def count_errors(funcs):
    exceptions_counter = 0
    for func in funcs:
        try:
            func()
        except:
            exceptions_counter += 1
    return exceptions_counter
