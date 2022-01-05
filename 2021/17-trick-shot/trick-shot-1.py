# start: 2021-12-20T16:59:16Z
# target area: x=235..259, y=-118..-62
import re, math
L = input()
region = re.compile(r"x=([\-0-9]+)\.\.([\-0-9]+), y=([\-0-9]+)\.\.([\-0-9]+)")
x0,x1,y0,y1 = map(int, region.search(L).groups())
print("target area:",x0,x1,y0,y1)

vy0 = -y0
found = False
while vy0>=0 and not found: 	# vy0=1,   y0=-9, y1=-4, x0=18, x1=20
	vy0 -= 1
	print(f"Trying vy0={vy0}")
	stepsabove = 2*vy0+1 		# stepsabove = 3
	stepsbelow = 0 				# stepsbelow = 0
	y = 0 						# y = 0
	vy1 = -vy0-1 				# vy1 = -2
	while y>y1:
		y += vy1				# y = -2    		y = -5
		vy1 -= 1 				# vy1 = -3 			vy1 = -4
		stepsbelow += 1 		# stepsbelow = 1 	stepsbelow = 2
	while y>=y0: 									# -5 >= -9:                                  	# -9>=-9:
		k = stepsabove + stepsbelow					# k = 3+2 = 5 									k = 6
		print(f"After {k} steps at y={y}:")
		vx0 = x0//k # недолет						# vx0 = 18//5 = 3 								vx0 = 18//6=3
		vx1 = max(vx0 - k + 1, 0)					# vx1 = 0 										vx1 = 0
		kx = min(k, vx0+1)							# kx = min(5,4) = 4    							kx = min(6,4)=4
		x = (vx0 + vx1)*kx // 2 					# x = (3+0)*4//2 = 6 							x = 6
		while x < x0:								# 6 < 18:    	10<18:      15<18: 				6 < 18:    	10<18:      15<18: 				
			print(f"   Trying vx0={vx0}, after {kx} steps at {x}")
			vx0 += 1 								# vx0 = 4		vx0 = 5 	vx0 = 7				vx0 = 4		vx0 = 5 	vx0 = 7
			vx1 = max(vx0 - k + 1, 0)			    # vx1 = 0 		vx1 = 1 	vx1 = 3				vx1 = 0 	vx1 = 0 	vx1 = 2
			kx = min(k, vx0+1)                  	# kx=5 			kx=5 		kx=5				kx=5 		kx=6 		kx=6
			x = (vx0 + vx1)*kx // 2             	# x=4*5//2=10   x=6*5//2=15 x=10*5//2=25 --\	x=4*5//2=10 x=5*6//2=15 x=9*6//2=27 --\
		if x <= x1:                					# 25 > 20   <------------------------------/    27 > 20   <---------------------------/
			found = True	
			print(f"    Found vx0={vx0}, after {kx} steps at {x}!!!	")
			break
		else:
			print(f"    Tried vx0={vx0}, after {kx} steps at {x}, no solution")
		y += vy1	 								# y = -9 										y = -14
		vy1 -= 1 									# vy1 = -5										vy1 = -6
		stepsbelow += 1 							# stepsbelow = 3 								stepsbelow=4

	if found:
		break

if found: print(f"Max height {vy0*(vy0+1)//2} (at speed vy0={vy0})")

# end: 2022-01-05T09:29:16Z