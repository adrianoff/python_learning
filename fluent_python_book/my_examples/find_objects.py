from collections import namedtuple

Student = namedtuple('Student', ['name', 'age'])

o1 = Student('Vasia', 32)
o2 = Student('Katia', 24)
o3 = Student('Sveta', 13)
o4 = Student('Vasia', 32)

l = [o1, o2, o3, o4]

l2 = filter(lambda obj: obj.name == 'Vasia', l)
print(list(l2)[0])

f = next((obj for obj in enumerate(l) if obj[1].name == 'Vasia'), None)
print(f)

print(next(enumerate(l)))