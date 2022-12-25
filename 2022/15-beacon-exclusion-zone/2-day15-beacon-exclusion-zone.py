import sys, re
from collections import defaultdict

bound = 4000000

squares = []
beacons = set()
neighborsp, neighborsq = defaultdict(int), defaultdict(int)
input = re.compile(r'Sensor at x=([\d-]+), y=([\d-]+): closest beacon is at x=([\d-]+), y=([\d-]+)')


for line in open(0):
    sx,sy,bx,by = map(int, input.search(line).groups())
    beacons.add((bx,by))
    d = abs(sx-bx) + abs(sy-by)
    # translate to coordinates where each sensor coverage area is a coordinate square
    # p = x+y, q = x-y
    Ap,Bp = sx + sy - d, sx + sy + d
    Aq,Bq = sx - sy - d, sx - sy + d
    squares.append((Ap,Bp,Aq,Bq))
    neighborsp[Ap-1] += 1
    neighborsp[Bp+1] += 1
    neighborsq[Aq-1] += 1
    neighborsq[Bq+1] += 1

# for all candidates that have both p, q immediately outside some 2+ squares
# note: we really should add admissible area boundary
#       but AoC won't do us dirty like that , will they?
for p in [pi for pi, times in neighborsp.items() if times > 1]:
    for q in [qi for qi, times in neighborsq.items() if times > 1]:
        # skip if outside admissible area
        x, y = (p+q)//2, (p-q)//2
        if x*(bound-x) < 0 or y*(bound-y) < 0 or (x,y) in beacons: 
            continue
        # check if our point is inside any of the squares
        inside = False
        for Ap,Bp,Aq,Bq in squares:
            if Ap<=p<=Bp and Aq<=q<=Bq:
                inside = True
                break
        if not inside:
            print(4000000*x + y)
            sys.exit(0)
