import numpy as np
A = np.fromfile('input.txt', sep='\n')
print(sum((A>np.roll(A,1))[1:]) - (A[0]>A[-1]))