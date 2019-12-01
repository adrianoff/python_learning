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
    s1 = string[:len_string//2]
    if len_string % 2 == 0:
        s2 = string[(len_string//2):]
    else:
        s2 = string[(len_string // 2)+1:]

    if s1 == s2[::-1]:
        return True
    else:
        return False

#print(is_palindrom('ctabatc'))




