"""## --- Day 14: Regolith Reservoir ---
The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, and that doesn't make any sense. However, you do notice a little path that leads *behind* the waterfall.

Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and the signal definitely leads further inside.

As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!

Fortunately, your familiarity with analyzing the path of falling material will come in handy here. You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly *air* with structures made of *rock*.

Your scan traces the path of each solid rock structure and reports the `x,y` coordinates that form the shape of the path, where `x` represents distance to the right and `y` represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:
`498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
`

This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. (Specifically, the first path consists of a line of rock from `498,4` through `498,6` and another line of rock from `498,6` through `496,6`.)

The sand is pouring into the cave from point `500,0`.

Drawing rock as `#`, air as `.`, and the source of the sand as `+`, this becomes:
`
  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.
`

Sand is produced *one unit at a time*, and the next unit of sand is not produced until the previous unit of sand *comes to rest*. A unit of sand is large enough to fill one tile of air in your scan.

A unit of sand always falls *down one step* if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally *one step down and to the left*. If that tile is blocked, the unit of sand attempts to instead move diagonally *one step down and to the right*. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand *comes to rest* and no longer moves, at which point the next unit of sand is created back at the source.

So, drawing sand that has come to rest as `o`, the first unit of sand simply falls straight down and then stops:
`......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......*o*.#.
#########.
`

The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:
`......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
.....oo.#.
#########.
`

After a total of five units of sand have come to rest, they form this pattern:
`......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
....oooo#.
#########.
`

After a total of 22 units of sand:
`......+...
..........
......o...
.....ooo..
....#ooo##
....#ooo#.
..###ooo#.
....oooo#.
...ooooo#.
#########.
`

Finally, only two more units of sand can possibly come to rest:
`......+...
..........
......o...
.....ooo..
....#ooo##
...*o*#ooo#.
..###ooo#.
....oooo#.
.*o*.ooooo#.
#########.
`

Once all `*24*` units of sand shown above have come to rest, all further sand flows out the bottom, falling into the endless void. Just for fun, the path any new sand takes before falling forever is shown here with `~`:
`.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........
`

Using your scan, simulate the falling sand. *How many units of sand come to rest before sand starts flowing into the abyss below?*
"""
import sys, numpy as np

data = open(0).read()
d = np.array(list(map(int,data.replace(' -> ',',').replace('\n',',')[:-1].split(','))))
minx, maxx, miny, maxy = d[::2].min(), d[::2].max(), min(0,d[1::2].min()), d[1::2].max()

print(minx, maxx, miny, maxy)
m = np.zeros((maxy+1, maxx+1), dtype=np.int8)
rocks = [line.split(' -> ') for line in data.split('\n')[:-1]]

for wall in rocks:
    px, py = map(int, wall[0].split(','))
    for pair in wall[1:]:
        x, y = map(int, pair.split(','))
        i,i1 = sorted([py, y])
        j,j1 = sorted([px, x])
        m[i:i1+1, j:j1+1] = 1
        px, py = x, y

print(m[:,minx:maxx+1])

ans = 0
q =0
path = np.zeros((maxy+1, 2), dtype=np.uint32)
path[0,0], path[0,1], pathlast, i = 0, 500, 0, 0
while not i==maxy:
    i,j = path[pathlast]
    print(i,j)
    m[i,j] += 8
    print(m[:,minx:maxx+1], end='\n\n')
    m[i,j] -= 8
    while True:
        q +=1
        # if q==200: sys.exit(0)
        if i==maxy or (j>0 and j<maxx and m[i+1,j-1:j+2].all()):
            ans += 1
            m[i,j] = 2
            print(m[:,minx:maxx+1], end='\n\n')
            pathlast -= 1
            break
        m[i,j] += 3
        print(m[:,minx:maxx+1], end='\n\n')
        m[i,j] -= 3
        i += 1        
        if j>=0 and j<=maxx and m[i,j]:
            j -= 1
            if j>=0 and j<=maxx and m[i,j]:
                j += 2
        pathlast+=1
        path[pathlast] = np.array([i,j])
print(ans-1)
        