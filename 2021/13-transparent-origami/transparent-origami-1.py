#start: 2021-12-13T05:00:00Z
import numpy as np
C = []
F = []
data = True
for line in open(0):
    if line.strip()=="":
        data = False
    elif data:
        x,y = map(int, line.strip().split(','))
        C.append((x,y))
    elif not data:
        F.append(line.strip().split()[2].split('='))
        F[-1][1] = int(F[-1][1])

W,H = max([x+1 for x, y in C]), max([y+1 for x, y in C])
A = np.zeros((H,W), dtype='uint8')
how, at = F[0]
for x,y in C:
    A[y,x] = 1

print(H, W)

B = None
if how=='x':
    if at+1>=W-at:
        B = A[:,:at].copy()
        B += np.pad(A[:,at+1:],((0,0),(at-(W-at-1),0)))[:,::-1]
    else:
        B = A[:,at+1::-1].copy()
        B += np.pad(A[:, :at], ((0,0),(W-at-at-1,0)))
else:
    if at+1>=H-at:
        B = A[:at,:].copy()
        B += np.pad(A[at+1:,:],((at-(H-at-1),0),(0,0)))[::-1,:]
    else:
        B = A[at+1::-1,:].copy()
        B += np.pad(A[:,:at], ((W-at-at-1, 0),(0,0)))
B = B.clip(max=1)
print('\n'.join([''.join([".#"[_] for _ in L]) for L in B]))

print(B.sum())
#end: 2021-12-13T05:56:25Z