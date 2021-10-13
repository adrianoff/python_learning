from functools import wraps
from time import time
import random


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r took: %2.4f sec' % (f.__name__, te-ts))
        return result
    return wrap


def insert_sorting(arr: list):
    N = len(arr)
    swaps = 0
    iterations = 0
    for top in range(1, N):
        k = top
        iterations += 1
        while k > 0 and arr[k] < arr[k-1]:
            iterations += 1
            arr[k], arr[k-1] = arr[k-1], arr[k]
            k -= 1
            swaps += 1

    return swaps, iterations, arr


def merge_sorting(arr: list) -> list:
    if len(arr) > 1:
        l = merge_sorting(arr[0:int(len(arr)/2)])
        r = merge_sorting(arr[int(len(arr)/2):])

        lk = rk = 0
        merged_arr = []
        while lk < len(l) and rk < len(r):
            if l[lk] < r[rk]:
                merged_arr.append(l[lk])
                lk += 1
            else:
                merged_arr.append(r[rk])
                rk += 1

        while lk < len(l):
            merged_arr.append(l[lk])
            lk += 1
        while rk < len(r):
            merged_arr.append(r[rk])
            rk += 1

        return merged_arr

    else:
        return arr


if __name__ == '__main__':
    N = 100000000
    s1 = [random.randint(0, 100) for i in range(N)]

    ts = time()
    res = merge_sorting(s1)
    te = time()
    print('func:%r took: %2.4f sec' % ('merge sorting', te - ts))

    # ts = time()
    # insert_sorting(s1)
    # te = time()
    # print('func:%r took: %2.4f sec' % ('insert sorting', te - ts))
