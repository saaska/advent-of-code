"""## --- Part Two ---
As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation `a`. The goal is still the square marked `E`. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from *any square at elevation `a`* to the square marked `E`.

Again consider the example from above:
`*S*abqponm
abcryxxl
accsz*E*xk
acctuvwj
abdefghi
`

Now, there are six choices for starting position (five marked `a`, plus the square marked `S` that counts as being at elevation `a`). If you start at the bottom-left square, you can reach the goal most quickly:
`...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^
`

This path reaches the goal in only `*29*` steps, the fewest possible.

*What is the fewest steps required to move starting from any square with elevation `a` to the location that should get the best signal?*
"""
import sys, numpy as np, string, collections

ans = 0
data =  open('input').read().rstrip()
s, e = map(data.index, ('S', 'E'))
data = data.replace('S','a').replace('E','z')

H = np.array([[string.ascii_lowercase.index(ch) for ch in line] for line in data.split('\n')])
n, m = H.shape

si, sj = s // (m+1), s % (m+1)
ei, ej = e // (m+1), e % (m+1)

q = collections.deque([(ei,ej)])
status = np.zeros_like(H)
cost = np.ones_like(H) * (n+1)*(m+1)
cost[ei, ej] = 0
status[ei,ej] = 1

neighbors = [(0,1), (0,-1), (-1,0), (1,0)]
while q:
    i,j = q.popleft()
    status[i,j] = 2
    for vec in neighbors:
        i1 = i+vec[0]
        j1 = j+vec[1]
        if 0<=i1<n and 0<=j1<m and not status[i1,j1] and H[i,j] <= H[i1,j1]+1:
            cost[i1,j1] = cost[i,j] + 1
            q.append((i1,j1))
            status[i1,j1] = 1

print((cost[H==0].min()))
