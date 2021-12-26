#start: 2021-12-26T21:45:00Z

import numpy as np

L = [line for line in open('input.txt')]
numbers = [int(_) for _ in L[0].split(',')]
boards = ''.join([l for l in L[1:] if l.rstrip()])
A = np.fromstring(boards, sep=' ', dtype=np.uint8).reshape(-1,5,5)
marked = np.zeros_like(A, dtype=np.uint32)

done = False
for x in numbers:
	marked[A==x] = 1
	for axis in (1,2):
		bingo = np.any(marked.sum(axis=axis)==5, axis=1)
		if np.any(bingo):
			board = bingo.argmax()
			print((A[board][marked[board]==0].sum())*x)
			done=True
			break
	if done: break

#end: 2021-12-26T22:24:48Z