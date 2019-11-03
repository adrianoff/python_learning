import functools
from time_decorator import my_timeit


@functools.lru_cache()
@my_timeit
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(40))