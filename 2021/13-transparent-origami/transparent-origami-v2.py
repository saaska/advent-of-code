#start: 2021-12-13T05:00:00Z

import numpy as np
dots, folds = open('input.txt') .read().split('\n\n')
C = np.fromstring(dots.replace(',',' '), sep=' ', dtype='uint16')
C = C.reshape(-1,2).T[::-1]
A = np.zeros(C.max(axis=1)+1, dtype='uint8')
A[C[0],C[1]] = 1
for step, cmd in enumerate(folds.rstrip().split('\n')):
    dim = "yx".index(cmd[11])
    at = A.shape[dim]//2
    if dim==1:
        A = (A[:, :at] + A[:, :-at-1:-1]).clip(max=1)
    else:
        A = (A[:at, :] + A[:-at-1:-1, :]).clip(max=1)
    if step==0: 
        print('Part 1:', A.sum(), '\nPart 2:')
print('\n'.join([''.join([" #"[_] for _ in r]) for r in A]))

#Part 1 end: 2021-12-13T05:56:25Z
#Part 2 end: 2021-12-13T06:03:09Z