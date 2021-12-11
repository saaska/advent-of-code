# start: 2021-12-11T09:26:35.57Z
import numpy as np

E = np.genfromtxt('input.txt',delimiter=1,dtype=np.uint8)
h, w = E.shape
Neighbors = np.pad(np.pad(np.array([[0]], dtype=np.uint8), 1, constant_values=1), [(0,h-1),(0,w-1)])
steps = 0
while E.any():
	steps += 1
	E += 1
	flashes = E>9
	while flashes.any():
		for i,j in zip(*np.where(flashes)):
			E[i,j] = 0
			E += np.sign(E) * np.roll(Neighbors, (i,j), axis=(0,1))[1:-1, 1:-1]
		flashes = E>9
print(steps)
# end: 2021-12-11T09:32:36Z