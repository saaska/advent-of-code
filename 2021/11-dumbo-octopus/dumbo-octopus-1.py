# start: 2021-12-11T07:48:34Z
import numpy as np

E = np.genfromtxt('input.txt',delimiter=1,dtype=np.uint8)
h, w = E.shape
Neighbors = np.pad(np.pad(np.array([[0]], dtype=np.uint8), 1, constant_values=1), [(0,h-1),(0,w-1)])
total = 0
for _ in range(100):
	E += 1
	flashes = E>9
	while flashes.any():
		for i,j in zip(*np.where(flashes)):
			total += 1
			E[i,j] = 0
			E += np.sign(E) * np.roll(Neighbors, (i,j), axis=(0,1))[1:-1, 1:-1]
		flashes = E>9
print(total)
# end: 2021-12-11T09:26:35.57Z