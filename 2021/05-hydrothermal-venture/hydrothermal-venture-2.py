# start: 2021-12-29T07:08:30Z

import numpy as np

L = open('input.txt').read().replace(' -> ',',').replace('\n',',')
P = np.fromstring(L, sep=',', dtype=np.int16).reshape(-1,4)

W,H = P[:,1::2].max()+1, P[:,::2].max()+1
Z = np.zeros((H,W), dtype=np.uint16)

print(len(Z[Z>1]))

for line, row in enumerate(P):
	print("line:", line+1, "row:", *row)
	j,i,J,I = row
	(i,j),(I,J) = sorted([(i,j),(I,J)])
	if (I-i)!=0 and (J-j)!=0:
		di = 1 - 2*(i>I)
		dj = 1 - 2*(j>J)
		for k in range(abs(I-i+1)):
			Z[i+k*di,j+k*dj] += 1
	else:
		Z[i:I+1, j:J+1] += 1
	print(len(Z[Z>1]))

print(len(Z[Z>1]))

#end: 