import functools


def cache(func):
    mydict = dict()

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        key = f"{func.__name__}{args}{kwargs}"
        if key not in mydict:
            mydict[key] = func(*args, **kwargs)
        return mydict[key]

    return wrapped_func


@cache
def fibonacci(num):
    if num <= 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(50))
print(fibonacci(60))
print(fibonacci(70))
print(fibonacci(80))
print(fibonacci(100))