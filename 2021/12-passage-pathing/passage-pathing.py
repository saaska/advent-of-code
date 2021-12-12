from string import ascii_uppercase as UC, ascii_lowercase as LC
from collections import defaultdict

TASK = 2 # 
A, visited = defaultdict(list), defaultdict(int)

def dfs(v, twice):
    if v=='end': return 1
    visited[v] += 1
    paths = 0
    for u in A[v]:
        if u[0] in UC or u[0] in LC and not visited[u]:
            paths += dfs(u, twice)
        elif TASK==2 and u != 'start' and not twice:
            paths += dfs(u, twice=True)
    visited[v] -= 1
    return paths

for line in open(0):
    u, v = line.rstrip().split('-')
    A[u].append(v)
    A[v].append(u)

print(dfs('start', twice=False))