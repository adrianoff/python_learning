import functools
from fluent_python_book.decorators7.time_decorator import my_timeit


@my_timeit
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(30))
