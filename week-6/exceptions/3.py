def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return 'missing'
    
