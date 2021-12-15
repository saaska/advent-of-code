# start: 2021-12-15T05:00:00Z

import numpy as np
INF = 1<<15
SHIFTS = [(1,0), (0,1), (-1,0), (0,-1)]
R = np.array([[_ for _ in map(int, line.rstrip())] 
	           for line in open(0)], dtype=np.uint16)
h,w = R.shape
risk = np.ones_like(R, dtype=np.uint16) * INF
risk[0,0] = 0
opn = {(0,0): True}
frzn = np.zeros_like(R, dtype=np.bool)
maxl = 0
while len(opn)>0 and not frzn[h-1,w-1]:
	maxl = max(len(opn), maxl)
	r, node = min([(risk[node], node) 
		            for node,_ in opn.items()])
	frzn[node] = True
	i,j = node
	neighbors = np.array([(i+di, j+dj) for  di, dj in SHIFTS
                         if i+di in range(0,h) and j+dj in range(0,w) 
                            and not frzn[i+di,j+dj]])
	for ii,jj in neighbors:
		risk[ii,jj] = min(risk[ii,jj], r + R[ii,jj])
		opn[ii,jj] = True
	del opn[node]

print(risk[h-1,w-1])

#end: 2021-12-15T06:40:35Z   misunderstood as DP prob where only moving rigt and down is allowed
