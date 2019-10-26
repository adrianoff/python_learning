import functools
from time_decorator import my_timeit

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

@my_timeit
print(fibonacci(30))
