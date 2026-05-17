def retry(func, n):
    for i in range(n):
        try:
            return func()
        except:
            if i == n-1:
                raise 




