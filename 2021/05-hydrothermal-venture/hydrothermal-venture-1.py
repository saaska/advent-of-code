# start: 2021-12-29T06:04:51Z

import numpy as np

L = open('input.txt').read().replace(' -> ',',').replace('\n',',')
P = np.fromstring(L, sep=',', dtype=np.int16).reshape(-1,4)

W,H = P[:,1::2].max()+1, P[:,::2].max()+1
Z = np.zeros((H,W), dtype=np.uint16)

print(len(Z[Z>1]))

for row in P:
	j,i,J,I = row
	if J<j:
		j,J = J,j
	if I<i:
		i,I = I,i
	if (I-i)>0 and (J-j)>0: continue
	Z[i:I+1, j:J+1] += 1
	print(len(Z[Z>1]))

print(len(Z[Z>1]))

#end: 2021-12-29T07:08:30Z