#start 2021-12-15T06:40:35Z
import numpy as np
INF = 1<<15
SHIFTS = [(1,0), (0,1), (-1,0), (0,-1)]
r = np.array([[_ for _ in map(int, line.rstrip())] for line in open(0)])
h,w = r.shape

R = np.zeros((5*h,5*w), dtype=np.uint8)
for i in range(5):
	for j in range(5):
		if not (i or j):
			R[:h,:w] = r
		elif not j:
			R[i*h:(i+1)*h, :w] = R[(i-1)*h:i*h, :w] % 9 + 1
		else:
			R[i*h:(i+1)*h, j*w:(j+1)*w] = R[i*h:(i+1)*h, (j-1)*w:j*w] % 9 + 1

h,w = R.shape
risk = np.ones_like(R, dtype=np.uint16) * INF
risk[0,0] = 0
opn = {(0,0): True}
frzn = np.zeros_like(R, dtype=np.bool)
it=0
maxl = 0
while len(opn)>0 and not frzn[h-1,w-1]:
	it+=1
	if it%100==0:
		print(f"it={it}, maxl{maxl}")
	maxl = max(len(opn), maxl)
	r, node = min([(risk[node], node) for node,_ in opn.items()])
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
print(R.shape)

#end: 2021-12-15T07:18:55Z
