# end: 2022-01-05T09:29:16Z
# target area: x=235..259, y=-118..-62
import re, math
L = input()
region = re.compile(r"x=([\-0-9]+)\.\.([\-0-9]+), y=([\-0-9]+)\.\.([\-0-9]+)")
x0,x1,y0,y1 = map(int, region.search(L).groups())
print("target area:",x0,x1,y0,y1)

minvx0 = 0
while minvx0*(minvx0+1)//2 < x0:
	minvx0 += 1

vy0 = -y0-1
found = set()
while vy0>=y0-1:
	print(f"Trying vy0={vy0}")
	y = 0
	k = 0
	vy1 = vy0
	while y>y1:
		print(y,end=' -> ')
		y += vy1
		vy1 -= 1
		k += 1
	print()
	while y>=y0:
		print(f"    After {k} steps at {y}:")
		vx0 = minvx0
		vx1 = max(vx0 - k + 1, 0)
		kx = min(k, vx0+1)
		x = (vx0 + vx1)*kx // 2
		while x < x0:
			print(f"       Trying vx0={vx0}, after {kx} steps at {x}")
			vx0 += 1
			vx1 = max(vx0 - k + 1, 0)
			kx = min(k, vx0+1)
			x = (vx0 + vx1)*kx // 2
		while x <= x1:
			if (vx0,vy0) not in found:
				found.add((vx0,vy0))
				print(f"        Found vx0={vx0}, after {kx} steps at {x}, v=({vx0},{vy0}), total found {len(found)}!!!	")
			vx0 += 1
			vx1 = max(vx0 - k + 1, 0)
			kx = min(k, vx0+1)
			x = (vx0 + vx1)*kx // 2
		else:
			print(f"        Tried vx0={vx0}, after {kx} steps at {x}, done ")
		y += vy1
		vy1 -= 1
		k += 1
	vy0 -= 1

print(f"Total found: {len(found)}")

# end: 2022-01-05T10:23:27Z
