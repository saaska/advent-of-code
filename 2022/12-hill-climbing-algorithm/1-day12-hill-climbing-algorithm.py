"""## --- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where `a` is the lowest elevation, `b` is the next-lowest, and so on up to the highest elevation, `z`.

Also included on the heightmap are marks for your current position (`S`) and the location that should get the best signal (`E`). Your current position (`S`) has elevation `a`, and the location that should get the best signal (`E`) has elevation `z`.

You'd like to reach `E`, but to save energy, you should do it in *as few steps as possible*. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be *at most one higher* than the elevation of your current square; that is, if your current elevation is `m`, you could step to elevation `n`, but not to elevation `o`. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:
```
*S*abqponm
abcryxxl
accsz*E*xk
acctuvwj
abdefghi
```

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the `e` at the bottom. From there, you can spiral around to the goal:
```
v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
```

In the above diagram, the symbols indicate whether the path exits each square moving up (`^`), down (`v`), left (`<`), or right (`>`). The location that should get the best signal is still `E`, and `.` marks unvisited squares.

This path reaches the goal in `*31*` steps, the fewest possible.

*What is the fewest steps required to move from your current position to the location that should get the best signal?*
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

q = collections.deque([(si,sj)])
status = np.zeros_like(H)
cost = np.ones_like(H) * (n+1)*(m+1)
cost[si, sj] = 0
status[si,sj] = 1

neighbors = [(0,1), (0,-1), (-1,0), (1,0)]
while q:
    i,j = q.popleft()
    status[i,j] = 2
    for vec in neighbors:
        i1 = i+vec[0]
        j1 = j+vec[1]
        if 0<=i1<n and 0<=j1<m and not status[i1,j1] and H[i1,j1] <= H[i,j]+1:
            cost[i1,j1] = cost[i,j] + 1
            q.append((i1,j1))
            status[i1,j1] = 1

print(cost[ei,ej])
