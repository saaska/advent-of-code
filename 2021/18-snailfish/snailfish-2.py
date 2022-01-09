# start: 2022-01-09T09:52:21Z
import json, re, sys, copy
L = [json.loads(line) for line in open(sys.argv[1])]
num = re.compile('\\d+')
num2 = re.compile('\\d\\d+')

def leftmost4deep(L, depth):
	# find a pair such that pair[idx] has depth 4
	if type(L)!=list:
		return None, None
	if depth==3:
		if type(L[0]) == list:
			return L, 0
		elif type(L[1]) == list:
			return L, 1
		else:
			return None, None
	else:
		pair, idx = leftmost4deep(L[0], depth+1)
		if pair is not None:
			return pair, idx
		else:
			return leftmost4deep(L[1], depth+1)

def add(L, M):
	# add two snailfish numbers and reduce the result
	N = copy.deepcopy([L,M])
	reducible = True
	while reducible:
		reducible = False
		pair, idx = leftmost4deep(N, 0)
		if pair is not None:
			# explode
			l, r = pair[idx]
			reducible = True
			pair[idx] = -1
			txt = json.dumps(N)
			i = txt.index('-1')
			left, right = num.search(txt[:i][::-1]), num.search(txt[i+2:])
			if left:
				lnew, (lcut0, lcut1) = str(int(left.group(0)[::-1]) + l), left.span() 
				lcut0, lcut1 = i-lcut1, i-lcut0
			else:
				lnew, lcut0, lcut1 =  '', 0, 0
			if right: 
				rnew, (rcut0, rcut1) = str(int(right.group(0)) + r), right.span() 
				rcut0, rcut1 = i+2+rcut0, i+2+rcut1
			else:
				rnew, rcut0, rcut1 =  '', len(txt)-1, len(txt)-1
			txt = (txt[:lcut0] + lnew + txt[lcut1:rcut0] + rnew + txt[rcut1:]).replace('-1','0')
			N = json.loads(txt)
		else:
			# search for numbers 10+, split
			txt = json.dumps(N)
			match = num2.search(txt)
			if match:
				reducible = True
				m = int(match.group(0))
				N = json.loads(txt.replace(match.group(0), json.dumps([m//2, m-m//2]), 1))
	return N 


def magnitude(L):
	if type(L) != list:
		return L
	else:
		return 3*magnitude(L[0]) + 2*magnitude(L[1])

i, maxmag = 0, 0
for A in L:
	for B in L:
		C = add(A, B)
		maxmag = max(maxmag, magnitude(C))
		i += 1
		if i%100 == 0:
			print('.', end='')


print(maxmag)

#end: 2022-01-09T10:08:55Z
