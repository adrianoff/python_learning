# n = 10
# for a in range(1, n):
#     for b in range(1, n):
#         for c in range(1, n):
#             for d in range(1, n):
#                 if pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3):
#                     print(a, b, c, d)
#                     break

# string = 'abcda'
# for i, char1 in enumerate(string):
#     for k, char2 in enumerate(string):
#         if char1 == char2 and i != k:
#             print('False')


# string = 'Mr Adrianov is happy    '
# print('%20'.join(string.split()))
from collections import OrderedDict


def is_palindrom(string):
    len_string = len(string)
    s1 = string[:len_string // 2]
    if len_string % 2 == 0:
        s2 = string[(len_string // 2):]
    else:
        s2 = string[(len_string // 2) + 1:]

    if s1 == s2[::-1]:
        return True
    else:
        return False


# print(is_palindrom('ctabatc'))

def one_mistake_between_strings(s1: str, s2: str):
    if s1 == s2:
        return True

    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) < len(s2):
        s1, s2 = s2, s1

    for i, c in enumerate(s1):
        s = s1[:i] + s1[i+1:]
        if s == s2:
            return True

    if len(s1) == len(s2):
        for i, c in enumerate(s1):
            for b in range(ord('a'), ord('z')+1):
                character = chr(b)
                s = list(s1)
                s[i] = character
                s = ''.join(s)

                if s == s2:
                    return True

    return False


def my_zip(string):
    my_dict = OrderedDict()
    for char in string:
        my_dict[char] = my_dict.setdefault(char, 0) + 1

    new_string = ''
    for key in my_dict.keys():
        count = my_dict[key]
        if count > 1:
            new_string += key + str(my_dict[key])
        else:
            new_string += key

    return new_string


def my_zip2(string):
    prev = None
    new_str = ''
    c = 1
    for char in string:
        if prev == char:
            c += 1
        if prev != char and prev is not None:
            if c > 1:
                new_str += prev + str(c)
            else:
                new_str += prev
            c = 1

        prev = char

    if c > 1:
        new_str += char + str(c)
    else:
        new_str += char

    return new_str


import math
def simple_number(start, stop):
    result = []
    for i in range(start, stop+1):
        flag = False
        for k in range(2, math.ceil(math.sqrt(i))+1):
            if i % k == 0:
                flag = True
                break

        if not flag:
            result.append(i)
    return result


def find_len_of_1(ll):
    """ Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину. """
    m = 0
    c = 0
    for i in ll:
        if i == 1:
            c += 1
            m = max(m, c)
        else:
            c = 0

    return m


def test_functions(func: callable):
    print(func.__doc__)

    arg1 = 'ddddabcdd'
    result = func(arg1)
    print(result)
    print('OK' if result == 'd4abcd2' else 'Fail')


#test_functions(my_zip2)
#print(simple_number(1, 20))

# print(find_len_of_1([0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0]))
# print(find_len_of_1([]))
# print(find_len_of_1([1, 1, 1, 1, 1, 1]))
# print(find_len_of_1([0, 0, 0, 0, 0, 0, 0]))


def checkio(data: str) -> bool:
    if len(data) < 10:
        return False

    has_digit = False
    has_upper = False
    has_lower = False
    for c in data:
        if str.isdigit(c):
            has_digit = True
        if str.islower(c):
            has_lower = True
        if str.isupper(c):
            has_upper = True

    return has_digit and has_upper and has_lower
