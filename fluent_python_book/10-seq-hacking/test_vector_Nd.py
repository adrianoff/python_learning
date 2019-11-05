import numpy as np
from vector_Nd import Vector

v1 = Vector([3, 4])
v2 = Vector([5, 6])

v3 = v1 + v2
v4 = v1 - v2

v5 = np.array([1, 2, 2])
v6 = np.array([1, 4, 4])

c = np.multiply(v5, v6)

print(c)

print(repr(v3))
print(repr(v4))
