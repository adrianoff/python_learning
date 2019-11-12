def cache_dec(func):
    prev_result = None

    def wrapper(*args, **kwargs):
        nonlocal prev_result
        if prev_result is None:
            prev_result = func(*args, **kwargs)

        return prev_result

    return wrapper

@cache_dec
def my_func():
    print('my_func call')
    return 0


print(my_func())
print(my_func())
