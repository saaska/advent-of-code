# start: 2022-01-11T08:55:30Z
import numpy as np

KERNEL = 2**np.arange(8,-.1,-1, dtype=np.uint32).reshape(3,3)

def main(file='input.txt'):
	lines = [line.rstrip() for line in open(file)]
	flt, _, *img = [list(map(".#".index, l)) for l in lines]
	flt = np.array(flt,dtype=np.uint32)
	img = np.array(img,dtype=np.uint32)
	for it in range(50):
		H,W = img.shape
		img = np.pad(img, ((2,2),(2,2)), constant_values=flt[0]*it%2)
		newimg = np.zeros((H+2,W+2),dtype=np.uint32)
		for i in range(H+2):
			for j in range(W+2):
				newimg[i,j] = flt[(img[i:i+3,j:j+3]*KERNEL).sum()]
		img = newimg
	print(newimg.sum())

if __name__ == '__main__':
	main(0)

# end: 2022-01-11T08:58:22Z
