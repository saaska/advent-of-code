#start:2021-12-14T05:00.00
import numpy as np
from collections import Counter
from operator import itemgetter

L = open(0).readlines()
s = L[0].strip()
R = {p[0]:p[2] for p in [_.split() for _ in L[2:]]}

print(s+'\n')

for step in range(10):
	I = [R.get(s[i:i+2],'') for i in range(len(s)-1)]
	I.append('')
	s = ''.join([s[i]+I[i] for i in range(len(s))])

c = Counter(s)
mM = sorted([(f, p) for p,f in freq.items()])
print(mM[-1][1]-mM[0][1])
#end:2021-12-14T05:15:39Z

