from random import shuffle

l = [3, 3, 5, 0, 2, 8, 19, -1]
print(l.sort())
print(l)

t = (3, 111, 3, 5, 1, 0)
print(type(sorted(t)))

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))

fruits.sort()
print(fruits)