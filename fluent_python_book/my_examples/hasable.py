class b(int):
    __hash__ = None

a = b()
b = 3
b.__hash__ = None
hash(b)
