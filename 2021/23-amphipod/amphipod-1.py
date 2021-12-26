# start: 2021-12-23T07:18:49Z
"""
0 1 . 2 . 3 . 4 . 5 6
    7   8   9  10
   11  12  13  14
"""

from math import nan as NaN
FIRSTROOM = 7
ROOMS = 4
HALL_ENDS = [0, FIRSTROOM-1]
PLACES = range(FIRSTROOM + ROOMS*2)

in_room = lambda place: place >= FIRSTROOM
above = lambda place: place - ROOMS
lowerfloor = lambda place: place >= FIRSTROOM + ROOMS
samekind = lambda ch1,ch2: ch1.lower()==ch2.lower()
PRICE = {ch: [1,10,100,1000]["ABCD".index(ch)] for ch in "ABCD"}
PRICE.update({ch: [1,10,100,1000]["abcd".index(ch)] for ch in "abcd"})
DEBUG = False
nextstop = None

def destination(ch):
	return 11+"abcd".index(ch.lower())

def sideblocked(place, Map):
	return place in HALL_ENDS and Map[place+(-1)**HALL_ENDS.index(place)]!='.'

def printmap(Map, lvl=0):
	print(f'{" "*2*lvl}#' + ''.join([Map[i] + ('.' if i>0 and i<5 else '') for i in range(FIRSTROOM)]) + '#')
	print(f'{" "*2*lvl}###' + ''.join([Map[i] + '#' for i in range(FIRSTROOM, FIRSTROOM+ROOMS)]) + '##')
	print(f'{" "*2*lvl}  #' + ''.join([Map[i] + '#' for i in range(FIRSTROOM+ROOMS, FIRSTROOM+2*ROOMS)]) + '  ')
	print()

def search(Map, seen, spent, best_solution, lvl=0):
	# global DEBUG, nextstop
	# if lvl==1 and Map[2].lower()=='b' or lvl==nextstop:
	# 	DEBUG = True	
	# if DEBUG:
	# 	print(f"{' '*2*lvl}lvl: {lvl}, current best: {best_solution}, spent: {spent}")
	# 	print(f"{' '*2*lvl}seen: {seen}")
	# 	print(f"{' '*2*lvl}Map: {Map}")
	# 	printmap(Map,lvl)
	# 	s = input()
	# 	if s and s in '1234567890':
	# 		DEBUG = False
	# 		nextstop = int(s)
	if Map=="b.Bc......daDCA":
		pass
	if Map[FIRSTROOM:].lower() == 'abcdabcd':
		print("Found solution, cost =", spent)
		return spent
	solution = best_solution
	for src in [p for p in PLACES if Map[p]!='.']:
		if (lowerfloor(src) and Map[above(src)]!='.' or  # blocked from above
			sideblocked(src, Map)): 	
			continue
		mover = Map[src]
		price = PRICE[mover]
		if in_room(src):
			# don't move if already in place
			if src+ROOMS==destination(mover) and samekind(mover, Map[src+ROOMS]) or \
			   src == destination(mover):
				continue
			for moving_right in (0, 1):
				# move up to hallway and to side
				add_spend = (2 + lowerfloor(src)) * price
				dst = 1 + (src-FIRSTROOM) % ROOMS + moving_right
				# continue moving to that side until blocked or spend too much
				while Map[dst]=='.' and not spent+add_spend >= solution:
					newmap = Map.replace(mover,'.')
					newmap = newmap[:dst]+mover+newmap[dst+1:]
					if newmap not in seen or spent+add_spend < seen[newmap]:
						seen[newmap] = spent+add_spend
						newsol = search(newmap, seen, spent+add_spend, solution, lvl+1)
						solution = min(newsol, solution)
					if dst in HALL_ENDS: break
					dst += -1 + 2*moving_right
					add_spend += (2 - (dst in HALL_ENDS)) * price
		else:
			dst = destination(mover)
			# check we can get to destination room
			rgt = 2 + (dst-FIRSTROOM) % ROOMS
			waypoints = ([pos for pos in 
			             range(src+1, rgt)] if src < rgt else
			            [pos for pos in 
			             range(rgt, src)])
			if any([Map[pos]!='.' for pos in waypoints]):
				continue
			# check no wrong kind roommates in room
			if any([Map[pos]!='.' and not samekind(mover, Map[pos]) for pos in [dst, dst - ROOMS]]):
				continue
			# if lower level taken, move to upper lvl
			if Map[dst]!='.': dst-= ROOMS
			# price from hallway into destination room
			add_spend = lowerfloor(dst) * price
			# price along the hallway
			if src < rgt:
				add_spend += 2*(rgt-src)*price
			else:
				add_spend += 2*(src-rgt+1)*price
			if src in HALL_ENDS:
				add_spend -= price
			if spent + add_spend > solution:
				continue
			newmap = Map.replace(mover,'.')
			newmap = newmap[:dst]+mover+newmap[dst+1:]	
			if newmap not in seen or spent+add_spend < seen[newmap]:
				seen[newmap] = spent+add_spend
				newsol = search(newmap, seen, spent+add_spend, solution, lvl+1)
				solution = min(newsol, solution)
	return solution

def main():
	L = open('input.txt').read().split('\n')[2:4]
	Map = '.'*7 + (L[0][3:10:2] + L[1][3:10:2]).replace('A', 'a', 1).replace('B', 'b', 1).replace('C', 'c', 1).replace('D', 'd', 1)
	seen = {}
	print(search(Map, {}, 0, (4*ROOMS+2)*1000))


if __name__ == '__main__':
	main()

# end: 2021-12-26T16:26:33Z
