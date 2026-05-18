def most_frequent_value(d):
    values = list(d.values())
    values.sort()
    frequent_val = None
    strike = 0
    max_strike = 0
    last_val = None
    for val in values:
        if val != last_val:
            if strike > max_strike:
                max_strike = strike
                frequent_val = last_val
            last_val = val
            strike = 0
        strike += 1
    return frequent_val
