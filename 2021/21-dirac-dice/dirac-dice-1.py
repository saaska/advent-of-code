"""Player 1 starting position: 8
Player 2 starting position: 5"""

pos, score = [], [0,0]
for i in (0,1):
	pos.append(int(input().split()[-1]))

dice = 1
for i in [0,1]*10000:
	pos[i] = (pos[i] + 3*dice+3 - 1) % 10 + 1
	score[i] += pos[i]
	# print(f"Player {i} rolls {dice}+{dice+1}+{dice+2} and moves to space {pos[i]} for a total score of {score[i]}")
	dice += 3
	if score[i]>=1000: break

print(score[score[0]==1000] * (dice-1))