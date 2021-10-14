from time import time
import random


def qsorting(L: list) -> list:
    if len(L) <= 1:
        return L
    pivot = L.pop()
    lL = [el for el in L if el < pivot]
    rL = [el for el in L if el >= pivot]
    return qsorting(lL) + [pivot] + qsorting(rL)


if __name__ == '__main__':
    N = 100
    s1 = [random.randint(0, 100) for i in range(N)]

    print(s1)
    ts = time()
    res = qsorting(s1)
    te = time()
    print('func:%r took: %2.4f sec' % ('merge sorting', te - ts))
    print(res)
