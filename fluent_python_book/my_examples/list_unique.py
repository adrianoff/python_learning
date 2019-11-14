from itertools import groupby
import numpy as np

ll = [1, 2, [1, 2, 3], 'string', 2, object()]

print(list(groupby(ll)))