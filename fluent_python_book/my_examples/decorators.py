import functools

def dec(f):
    return f

@dec
@functools.lru_cache()
def func(x):
    return x+1


func(1)

