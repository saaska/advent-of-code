import numpy as np
A = np.fromfile('input.txt', sep='\n')
A = np.convolve(A, np.ones(3))[2:-2]
print(sum((A>np.roll(A,1))[1:]))