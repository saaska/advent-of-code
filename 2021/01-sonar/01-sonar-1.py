import sys
prev = int(input())
ans = 0
for line in sys.stdin:
	cur = int(line)
	if cur > prev:
		ans+=1
	prev = cur
print(ans)