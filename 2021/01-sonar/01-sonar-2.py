import sys
a,b,c = int(input()), int(input()), int(input())
prevsum = a+b+c
ans = 0

for line in sys.stdin:
	cur = int(line.rstrip())
	a,b,c = b,c,cur
	cursum = a+b+c
	if cursum > prevsum:
		ans+=1
	prevsum = cursum
print(ans)