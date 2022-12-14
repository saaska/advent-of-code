"""## --- Part Two ---
You realize you misread the scan. There isn't an endless void at the bottom of the scan - there's floor, and you're standing on it!

You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a `y` coordinate equal to *two plus the highest `y` coordinate* of any point in your scan.

In the example above, the highest `y` coordinate of any point is `9`, and so the floor is at `y=11`. (This is as if your scan contained one extra rock path like `-infinity,11 -> infinity,11`.) With the added floor, the example above now looks like this:
`
        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
<-- etc #################### etc -->
`

To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at `500,0`, blocking the source entirely and stopping the flow of sand into the cave. In the example above, the situation finally looks like this after `*93*` units of sand come to rest:
`............o............
...........ooo...........
..........ooooo..........
.........ooooooo.........
........oo#ooo##o........
.......ooo#ooo#ooo.......
......oo###ooo#oooo......
.....oooo.oooo#ooooo.....
....oooooooooo#oooooo....
...ooo#########ooooooo...
..ooooo.......ooooooooo..
#########################
`

Using your scan, simulate the falling sand until the source of the sand becomes blocked. *How many units of sand come to rest?*
"""
import sys, numpy as np

data = open('input').read()
d = np.array(list(map(int,data.replace(' -> ',',').replace('\n',',')[:-1].split(','))))
maxy = d[1::2].max()

m = np.zeros((maxy+3, 500 + maxy + 2), dtype=np.int8)
walls = [line.split(' -> ') for line in data.split('\n')[:-1]]
for wall in walls:
    px, py = map(int, wall[0].split(','))
    for pair in wall[1:]:
        x, y = map(int, pair.split(','))
        i,i1 = sorted([py, y])
        j,j1 = sorted([px, x])
        m[i:i1+1, j:j1+1] = 1
        px, py = x, y

m[maxy+2] = 1 # floor

ans = 0
path = [(0, 500)]
while path:
    i,j = path[-1]
    while not m[i+1,j-1:j+2].all():
        i += 1        
        if m[i,j]:
            j -= 1
            if m[i,j]:
                j += 2
        path.append((i,j))
    ans += 1
    m[i,j] = 2
    path.pop()

print(ans)
        