# Квадратичные сортировки.


def bubble_sorting(arr):
    """ Bubble sorting """
    pass


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
    pass


def test_sorting(sorting_func):
    print(sorting_func.__doc__)

    print('Test case #1:', end='')
    arr = [4, 2, 4, 2, 1]
    arr_sorted = [1, 2, 2, 4, 4]
    sorting_func(arr)
    print('OK' if arr == arr_sorted else 'Fail')

    print('Test case #2:', end='')
    arr = list(range(10, 20)) + list(range(0, 10))
    arr_sorted = list(range(0, 20))
    sorting_func(arr)
    print('OK' if arr == arr_sorted else 'Fail')
    print("")


#test_sorting(bubble_sorting)
test_sorting(insert_sorting)
#test_sorting(choice_sorting)