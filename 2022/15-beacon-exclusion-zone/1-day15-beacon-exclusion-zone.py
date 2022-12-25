import sys

def mdist(x1,y1,x2,y2): return abs(x2-x1) + abs(y2-y1)

ylevel = 2000000
intervals = []
levelbeacons = set()
for line in open(0):
    #Sensor at x=489739, y=1144461: closest beacon is at x=-46516, y=554951
    words = line.replace(':','').replace(',','').replace('=',' ').split()
    #Sensor at x 489739 y 1144461 closest beacon is at x -46516 y 554951
    sx,sy,bx,by = map(int, [words[i] for i in (3,5,11,13)])
    if by == ylevel: levelbeacons.add(bx)
    d = mdist(sx,sy,bx,by)
    height = mdist(sx,sy,sx,ylevel)
    if height > d: continue
    # [a b] interval
    a = sx - (d-height)
    b = sx + (d-height)
    intervals.append((a,b))

intervals.sort()
print(intervals)
print(levelbeacons)
N = len(intervals)
i,j = 0,0
ans = 0
while i < N:
    A,B = intervals[i]
    while j<N and intervals[j][0]<=B:
        B = max(B, intervals[j][1])
        j += 1
    print(f'adding {B-A+1}, B={B}, A={A} minus {len([x for x in levelbeacons if A<=x<=B])} beacons')
    ans += (B-A+1) - len([x for x in levelbeacons if A<=x<=B])
    i = j
print(ans)
