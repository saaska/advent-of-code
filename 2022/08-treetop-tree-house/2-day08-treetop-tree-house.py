"""## --- Part Two ---
Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of *trees*.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle `5` in the second row:
`30373
25*5*12
65332
33549
35390
`

* Looking up, its view is not blocked; it can see `*1*` tree (of height `3`).
* Looking left, its view is blocked immediately; it can see only `*1*` tree (of height `5`, right next to it).
* Looking right, its view is not blocked; it can see `*2*` trees.
* Looking down, its view is blocked eventually; it can see `*2*` trees (one of height `3`, then the tree of height `5` that blocks its view).

A tree's *scenic score* is found by *multiplying together* its viewing distance in each of the four directions. For this tree, this is `*4*` (found by multiplying `1 * 1 * 2 * 2`).

However, you can do even better: consider the tree of height `5` in the middle of the fourth row:
`30373
25512
65332
33*5*49
35390
`

* Looking up, its view is blocked at `*2*` trees (by another tree with a height of `5`).
* Looking left, its view is not blocked; it can see `*2*` trees.
* Looking down, its view is also not blocked; it can see `*1*` tree.
* Looking right, its view is blocked at `*2*` trees (by a massive tree of height `9`).

This tree's scenic score is `*8*` (`2 * 2 * 1 * 2`); this is the ideal spot for the tree house.

Consider each tree on your map. *What is the highest scenic score possible for any tree?*
"""
import numpy as np, sys

f = [list(map(int, line.rstrip())) for line in sys.stdin]
a = np.array(f, dtype=np.uint8)

vdist = np.ones((4,)+a.shape, dtype=np.uint64)
vdist[:,0,:], vdist[:,-1,:], vdist[:,:,0], vdist[:,:,-1] = 0,0,0,0

for rot in range(4):
    n,m = a.shape
    for i in range(1,n-1):
        lastpos = np.zeros(10)
        lastpos[a[i,0]] = 0
        for j in range(1,m-1):
            vdist[rot, i, j] = j - lastpos[a[i,j]]
            lastpos[:a[i][j]+1] = j
    if rot % 2 == 0:
        a = a[:,::-1]
        vdist = vdist[:,:,::-1]
    else:
        a = a.T
        vdist = vdist.swapaxes(1,2)
print(np.max(vdist[0]*vdist[1]*vdist[2]*vdist[3]))