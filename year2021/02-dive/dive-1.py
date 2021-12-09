import sys
d = {'forward':0, 'down':0, 'up':0}
for line in sys.stdin:
	where, howmuch = line.split()
	d[where] += int(howmuch)

print(d['forward']*(d['down']-d['up']))