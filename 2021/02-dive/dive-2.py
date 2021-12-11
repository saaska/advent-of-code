import sys
x, y, aim = 0, 0, 0
for line in sys.stdin:
	where, howmuch = line.split()
	howmuch = int(howmuch)
	if where == 'forward':
		x += howmuch
		y += aim*howmuch
	elif where == 'up':
		aim -= howmuch
	else:
		aim += howmuch
	# print(line, x, y, aim)
print(x*y)