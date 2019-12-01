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


def test_functions(func: callable):
    print(func.__doc__)

    arg1 = 'pale'
    arg2 = 'bale'
    result = func(arg1, arg2)
    print('OK' if result is True else 'Fail')


test_functions(one_mistake_between_strings)
