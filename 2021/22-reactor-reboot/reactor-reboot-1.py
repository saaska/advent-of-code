import re, numpy as np, bisect
INPUTFORMAT = re.compile(r"(on|off) x=([\d\-]+)..([\d\-]+),y=([\d\-]+)..([\d\-]+),z=([\d\-]+)..([\d\-]+)")
NUMAXES=3
AXES = tuple(range(NUMAXES))
axshapes=[[1]*NUMAXES for ax in range(NUMAXES)]

cuts = [[-50, 51] for ax in AXES]
proc = []
for line in open(0):#"test1.txt"):
	g = INPUTFORMAT.match(line).groups()
	on = g[0]=="on"
	(*c,) = map(int, g[1:])
	add = True
	for ax in AXES:
		c[2*ax] = max(-50, c[2*ax])
		c[2*ax+1] = min(50, c[2*ax+1])+1
		if c[2*ax]>50 or c[2*ax+1]<=-50:
			add = False
	if not add: continue
	for ax in AXES:
		for j in (0,1):
			if c[2*ax+j] not in cuts[ax] : cuts[ax].append(c[2*ax+j])
	proc.append((on, c))			

for i, c in enumerate(cuts):
	c.sort()
	cuts[i] = np.array(c, dtype=np.int16)
	axshapes[i][i] = len(cuts[i])-1

blocks = np.zeros([axshapes[i][i] for i in AXES], dtype=np.uint8)

for on, x in proc:
	xyzmask = np.array(True, dtype=np.uint8).reshape([1 for _ in AXES])
	for axis in AXES:
		mask = (cuts[axis][:-1]>=x[2*axis]) * \
		       (cuts[axis][1:]<=x[2*axis+1])
		mask = mask.reshape(axshapes[axis])
		xyzmask = np.multiply(xyzmask, mask)
	blocks[xyzmask==1] = on

vol = np.ones((1,1,1), dtype=np.int64)
for axis in AXES:
	sides = (cuts[axis][1:]-cuts[axis][:-1]).reshape(axshapes[axis])
	vol = vol*sides

print((blocks*vol).sum())