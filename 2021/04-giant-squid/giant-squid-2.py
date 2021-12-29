#start: 2021-12-26T22:28:23Z

import numpy as np

L = [line for line in open('input.txt')]
numbers = [int(_) for _ in L[0].split(',')]
boards = ''.join([l for l in L[1:] if l.rstrip()])
A = np.fromstring(boards, sep=' ', dtype=np.uint8).reshape(-1,5,5)
orig_nums = '|'.join(map(str,range(1, A.shape[0]+1)))+'|'
marked = np.zeros_like(A, dtype=np.uint32)

for x in numbers:
	marked[A==x] = 1
	bingo = [np.any(marked.sum(axis=axis)==5, axis=1) for axis in (1,2)]
	bingo = bingo[0]|bingo[1]
	while np.any(bingo) and A.shape[0]>1:
		board = bingo.argmax()
		board_num = orig_nums.split('|')[board]
		A = np.concatenate([A[:board],A[board+1:]], axis=0)
		marked = np.concatenate([marked[:board],marked[board+1:]], axis=0)
		orig_nums = orig_nums.replace(board_num+'|', '', 1)
		bingo = [np.any(marked.sum(axis=axis)==5, axis=1) for axis in (1,2)]
		bingo = bingo[0]|bingo[1]
	if np.any(bingo) and A.shape[0]==1:
		print((A[0][marked[0]==0].sum())*x)
		break
#end: 2021-12-29T05:54:52Z