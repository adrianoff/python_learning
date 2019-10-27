from datetime import datetime


def my_timeit(func):
    calls = 1

    def wrapper(*args, **kwargs):
        nonlocal calls
        start = datetime.now()
        result = func(*args, **kwargs)
        print('Call ' + str(calls) + ' of ' + func.__name__, datetime.now() - start)
        calls = calls + 1
        return result
    return wrapper
