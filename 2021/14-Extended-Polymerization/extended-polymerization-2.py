#start:2021-12-14T05:15:39Z
from collections import Counter, defaultdict
L = open(0).readlines()
s = L[0].strip()
rules = {words[0]: words[2] \
         for words in [line.split() for line in L[2:]]}
pairs = [s[i:i+2] for i in range(len(s)-1)]
paircount = defaultdict(int, Counter(pairs))

for step in range(10):
	q = paircount.copy()
	for pair, count in paircount.items():
		if pair not in rules or count == 0: continue
		newchar = rules[pair]
		q[pair] -= count
		q[pair[0]+newchar] += count
		q[newchar+pair[1]] += count
	paircount = q

freq = defaultdict(int)
for pair,count in paircount.items():
	if count:
		freq[pair[0]]+=count
		freq[pair[1]]+=count
freq[s[0]]  += 1 
freq[s[-1]] += 1

Freq = sorted([(f, p) for p,f in freq.items()])
print((Freq[-1][0]-Freq[0][0])//2)
#end:2021-12-14T06:00:27Z

