# start: 2021-12-29T07:40:52Z
from collections import Counter
a = list(map(int, input().split(',')))
c = Counter(a)

for day in range(80):
	print(f"day {day}: {c}")
	d = {}
	for days in range(8):
		d[days] = c.get(days+1, 0)
	d[8] = c.get(0,0)
	d[6] += c.get(0,0)
	c = d

print(sum(c.values()))

# end: 2021-12-29T07:57:20Z


