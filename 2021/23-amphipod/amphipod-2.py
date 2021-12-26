# start: 2021-12-26T16:31:24Z
"""
0 1 . 2 . 3 . 4 . 5 6
    7   8   9  10
   11  12  13  14
   15  16  17  18
   19  20  21  22
"""
FIRST_ROOM = 7
ROOMS = 4
LAYERS = 4
HALL_ENDS = [0, FIRST_ROOM-1]
PLACES = range(FIRST_ROOM + ROOMS*LAYERS)
PRICE = {ch: [1,10,100,1000]["ABCD".index(ch)] for ch in "ABCD"}

in_room = lambda place: place >= FIRST_ROOM
lower_layer = lambda place: place >= FIRST_ROOM + ROOMS
in_place = lambda src, Map: (src-FIRST_ROOM) % ROOMS == "ABCD".index(Map[src])
pos_above = lambda place: place - ROOMS
roommate_set = lambda ch, Map: set(Map[FIRST_ROOM+"ABCD".index(ch)::4]) - {'.'}

def num_steps(pos_hall, pos_room):
	if pos_hall > pos_room:
		pos_hall, pos_room = pos_room, pos_hall
	vert = (pos_room - FIRST_ROOM) // 4 + 1
	hall_left = ((pos_room - FIRST_ROOM) % 4 + 1) 
	if hall_left >= pos_hall:
		horiz = (hall_left - pos_hall) * 2 + 1
	else:
		horiz = (pos_hall - hall_left) * 2 - 1
	if pos_hall in HALL_ENDS:
		horiz -= 1
	return vert + horiz

def destination(ch):
	return len(PLACES) - ROOMS + "ABCD".index(ch)

def sideblocked(place, Map):
	return place in HALL_ENDS and Map[place + 1 - 2*HALL_ENDS.index(place)]!='.'

def search(Map, cost, spent, best_solution, lvl=0):
	if Map[FIRST_ROOM:] == 'ABCD'*LAYERS:
		print("Found solution, cost =", spent)
		return spent
	solution = best_solution
	for src in [p for p in PLACES if Map[p]!='.']:
		if (lower_layer(src) and Map[pos_above(src)]!='.' or  # blocked from above
			sideblocked(src, Map)): 	
			continue
		mover = Map[src]
		moves = []
		if in_room(src):
			# don't move if already in correct room with correct roommates, if any
			rmmts = roommate_set(mover, Map)
			if in_place(src, Map) and rmmts<=set(mover):
				continue
			elif rmmts<=set(mover):
				# if can move to correct room, do it!
				moves = [destination(mover) - ROOMS * len(rmmts)]
			# try moving both ways to empty places in the hallway
			for moving_right in (0, 1):
				# first move up to hallway and to the side
				dst = 1 + (src-FIRST_ROOM) % ROOMS + moving_right
				# then continue moving to that side until blocked
				while Map[dst]=='.':
					moves.append(dst)
					if dst in HALL_ENDS: break
					dst += 2*moving_right - 1
		else:
			dst = destination(mover)
			# check hallway is not blocked
			lft = 1 + (dst-FIRST_ROOM) % ROOMS
			waypoints = (range(src+1, lft+1) if src <= lft else
			            range(lft+1, src))
			if any([Map[pos]!='.' for pos in waypoints]):
				continue
			# check no wrong kind roommates in room
			if not roommate_set(mover, Map)<=set(mover):
				continue
			# if lower level taken, move to upper lvl
			while Map[dst]!='.': dst -= ROOMS
			moves.append(dst)
		for dst in moves:
			newspent = spent + num_steps(src, dst) * PRICE[mover]
			if newspent > solution:
				continue
			newmap = Map[:src] + '.' + Map[src+1:]
			newmap = newmap[:dst] + mover + newmap[dst+1:]	
			if newmap not in cost or newspent < cost[newmap]:
				cost[newmap] = newspent
				newsol = search(newmap, cost, newspent, solution, lvl+1)
				solution = min(newsol, solution)
	return solution

def main():
	L = open('input.txt').read().split('\n')[2:4]
	Map = '.'*7 + L[0][3:10:2] + "DCBA" + "DBAC"+L[1][3:10:2] 
	cost = {}
	print(search(Map, {}, 0, LAYERS*ROOMS*len(PLACES)*1000))


if __name__ == '__main__':
	main()

# end: 2021-12-26T20:00:22Z
