def my_test_func(x):
    """function doc"""
    return x + 1.1


print(help(my_test_func))

print(list(map(my_test_func, range(10))))
