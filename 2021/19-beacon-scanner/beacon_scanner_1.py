import numpy as np

def have_common(A,B):
	# number of common elements in two sorted lists
	i,j,comm = 0,0,0
	while i<len(A) and j<len(B):
		if A[i] == B[j]:
			i += 1
			j += 1
			comm += 1
		elif A[i]<B[j]:
			i += 1
		else:
			j += 1
	return comm

def main(file='input.txt'):
	blocks = open(file).read().rstrip().split('\n\n')
	blocks = [blk.split('---\n')[1].replace(',',' ') for blk in blocks]
	blocks = [np.fromstring(blk, sep=' ',dtype='int32').reshape((-1,3)) 
			  for blk in blocks]
	
	Nsc = len(blocks)
	Nbc = [len(blk) for blk in blocks]
	maxbeacons = max(Nbc)

	# all distances between beacons seen by each scanner, sorted 
	dists = np.zeros((Nsc, maxbeacons*(maxbeacons-1)), dtype=np.int32)

	# distances from each beacon to oher beacons seen by each scanner, sorted 
	pdists = np.zeros((Nsc, maxbeacons, maxbeacons-1), dtype=np.int32)

	for i, B in enumerate(blocks):
		n = Nbc[i]
		for j in range(1,n):
			dists[i,(j-1)*n:j*n] = ((B-np.roll(B, -j, 0))**2).sum(axis=1)
		for j in range(n):
			pdists[i,j,:n] = sorted(dists[i,j:j+n*n:n])
		dists[i,:n*n-n].sort()

	# how many of dists are common between each pair of scanners
	comm_dists = np.zeros((Nsc, Nsc))
	for i in range(Nsc):
		for j in range(i+1, Nsc):
			n,m = Nbc[i], Nbc[j]
			comm_dists[i,j] = have_common(dists[i, :n*n-n], dists[j, :m*m-m])
	comm_dists += comm_dists.T

	# all 24 possible rotation transforms
	E = np.identity(3, dtype=np.int32)
	orts = np.concatenate([E, -E])
	transforms = np.zeros((24,3,3), dtype=np.int32)
	k = 0
	for x in orts:
		for y in orts:
			if np.linalg.matrix_rank(np.array([x,y]))==1: continue
			z = np.cross(x,y)
			transforms[k] = np.array([x,y,z])
			k += 1

	# the formula to get beacon coords v seen by each scanner to a common system
	# (of the very first scanner) is v.T + r, where T and r are specific to scanner
	# scoords is simply the collection of sets of common coords 
	# for the beacons seen by each scanner
	scoords = [None]*Nsc
	r,T = np.zeros((Nsc,3), dtype=np.int32), np.zeros((Nsc, 3, 3), dtype=np.int32)
	scoords[0] = set([tuple(b) for b in blocks[0]])
	r[0] = [0,0,0]
	T[0] = E
	anchored_sc = {0} # anchor the very first scanner
	free_sc = set(range(1, Nsc)) # all others unknown

	# try to find overlapping scanners first by comparing total distance lists
	# then if there is a overlap enough for 12x12 submatrix 
	# try to find the transform and origin vector
	def anchor_another():
		nonlocal free_sc
		for scanner_i in anchored_sc:
			for scanner_j in free_sc:
				if comm_dists[scanner_i, scanner_j] < 12*11: continue
				ni,nj = Nbc[scanner_i], Nbc[scanner_j]
				for i in range(ni*nj):
					beacon_i, beacon_j = i//nj, i%nj
					if have_common(pdists[scanner_i, beacon_i, :ni-1], 
						           pdists[scanner_j, beacon_j, :nj-1])>=11:
						for Tj in transforms:
							rj = - blocks[scanner_j][beacon_j].dot(Tj) \
							     + blocks[scanner_i][beacon_i].dot(T[scanner_i]) + r[scanner_i] 
							coords = rj + blocks[scanner_j].dot(Tj)
							coord_set = set([tuple(v) for v in coords])
							Nmatched = len(scoords[scanner_i].intersection(coord_set))
							if Nmatched>= 12:
								joined = True
								r[scanner_j] = rj
								T[scanner_j] = Tj
								scoords[scanner_j] = coord_set
								anchored_sc.add(scanner_j)
								free_sc -= {scanner_j}
								return True
		return False

	# attach through overlaps while we can
	while free_sc and anchor_another():
		pass

	if free_sc:
		print(f"failed to find anchor for scanners: {free_sc} (0-based)")
	else:
		beacons = set()
		for cset in scoords:
			beacons |= cset
		print(len(beacons))


if __name__ == '__main__':
	main()

#end: 2022-01-10T12:52:31Z
