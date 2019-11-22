# Квадратичные сортировки.


def bubble_sorting(arr):
    """ Bubble sorting """
    N = len(arr)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]


def insert_sorting(arr):
    """ Insert sorting """
    N = len(arr)
    for top in range(1, N):
        k = top
        while k > 0 and arr[k-1] > arr[k]:
            arr[k], arr[k-1] = arr[k-1], arr[k]
            k -= 1


def choice_sorting(arr):
    """ Choice sorting """
    N = len(arr)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if arr[k] < arr[pos]:
                arr[k], arr[pos] = arr[pos], arr[k]


def count_sorting(arr):
    """ Count sorting """
    N = len(arr)
    maximum = minimum = None
    for i in range(0, N):
        if maximum is None:
            maximum = arr[i]
        if minimum is None:
            minimum = arr[i]

        if arr[i] > maximum:
            maximum = arr[i]

        if arr[i] < minimum:
            minimum = arr[i]

    count_arr = [0] * (abs(maximum-minimum)+1)

    for i in range(0, N):
        v = arr[i]
        count_arr[abs(v-minimum)] += 1

    M = len(count_arr)
    arr[:] = []
    for i in range(0, M):
        arr += [i+minimum] * count_arr[i]


def test_sorting(sorting_func):
    print(sorting_func.__doc__)

    print('Test case #1:', end='')
    arr = [-10, 1, 2, 4, 2, 1, 10]
    arr_sorted = [-10, 1, 1, 2, 2, 4, 10]
    sorting_func(arr)
    print('OK' if arr == arr_sorted else 'Fail')

    print('Test case #2:', end='')
    arr = [4, 2, 4, 2, 1]
    arr_sorted = [1, 2, 2, 4, 4]
    sorting_func(arr)
    print('OK' if arr == arr_sorted else 'Fail')

    print('Test case #3:', end='')
    arr = list(range(10, 20)) + list(range(0, 10))
    arr_sorted = list(range(0, 20))
    sorting_func(arr)
    print('OK' if arr == arr_sorted else 'Fail')

    print('Test case #4:', end='')
    arr = [-10, -10000, 1]
    arr_sorted = [-10000, -10, 1]
    sorting_func(arr)
    print('OK' if arr == arr_sorted else 'Fail')


test_sorting(count_sorting)
#test_sorting(bubble_sorting)
#test_sorting(insert_sorting)
#test_sorting(choice_sorting)
