import numpy as np
A = np.genfromtxt(open(0), delimiter=1, dtype=np.uint8)
most_common = A.sum(axis=0) // np.ceil(len(A)/2)
x = int(''.join(map(str, map(int, most_common))), 2)
y = (1<<A.shape[1]) - x - 1
print(x*y)


