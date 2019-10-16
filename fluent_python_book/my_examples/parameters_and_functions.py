

def f(a):
    print(a, id(a), 'local')

b = 3
f(b)
print(b, id(b), 'global')



*a, b, c = [True, 11, 12]
print(a, b, c)