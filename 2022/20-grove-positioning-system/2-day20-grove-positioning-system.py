"""## --- Part Two ---

The grove coordinate values seem nonsensical. While you ponder the mysteries of Elf encryption, you suddenly remember the rest of the decryption routine you overheard back at camp.

First, you need to apply the *decryption key*, `811589153`. Multiply each number by the decryption key before you begin; this will produce the actual list of numbers to mix.

Second, you need to mix the list of numbers *ten times*. The order in which the numbers are mixed does not change during mixing; the numbers are still moved in the order they appeared in the original, pre-mixed list. (So, if -3 appears fourth in the original list of numbers to mix, -3 will be the fourth number to move during each round of mixing.)

Using the same example as above:
```Initial arrangement:
811589153, 1623178306, -2434767459, 2434767459, -1623178306, 0, 3246356612

After 1 round of mixing:
0, -2434767459, 3246356612, -1623178306, 2434767459, 1623178306, 811589153

After 2 rounds of mixing:
0, 2434767459, 1623178306, 3246356612, -2434767459, -1623178306, 811589153

After 3 rounds of mixing:
0, 811589153, 2434767459, 3246356612, 1623178306, -1623178306, -2434767459

After 4 rounds of mixing:
0, 1623178306, -2434767459, 811589153, 2434767459, 3246356612, -1623178306

After 5 rounds of mixing:
0, 811589153, -1623178306, 1623178306, -2434767459, 3246356612, 2434767459

After 6 rounds of mixing:
0, 811589153, -1623178306, 3246356612, -2434767459, 1623178306, 2434767459

After 7 rounds of mixing:
0, -2434767459, 2434767459, 1623178306, -1623178306, 811589153, 3246356612

After 8 rounds of mixing:
0, 1623178306, 3246356612, 811589153, -2434767459, 2434767459, -1623178306

After 9 rounds of mixing:
0, 811589153, 1623178306, -2434767459, 3246356612, 2434767459, -1623178306

After 10 rounds of mixing:
0, -2434767459, 1623178306, 3246356612, -1623178306, 2434767459, 811589153
```

The grove coordinates can still be found in the same way. Here, the 1000th number after `0` is `*811589153*`, the 2000th is `*2434767459*`, and the 3000th is `*-1623178306*`; adding these together produces `*1623178306*`.

Apply the decryption key and mix your encrypted file ten times. *What is the sum of the three numbers that form the grove coordinates?*
"""
import sys, numpy as np

A = [int(_)*811589153 for _ in open(0).readlines()]
N = len(A)
B = np.array(A)
loc, rloc = np.arange(N), np.arange(N)
print(B)
for step in range(10):
    for i, a in enumerate(A):
        pos = loc[i]
        newpos = (pos + (N-1) + a%(N-1)) % (N-1)
        if pos<newpos:
            B[pos:newpos], B[newpos] = B[pos+1:newpos+1], B[pos]
            loc[i] = newpos
            for j in range(pos+1, newpos+1):
                loc[rloc[j]] -= 1
            rloc[pos:newpos], rloc[newpos] = rloc[pos+1:newpos+1], rloc[pos]
        elif pos>newpos:
            B[newpos+1:pos+1], B[newpos] = B[newpos:pos], B[pos]
            loc[i] = newpos
            for j in range(newpos, pos):
                loc[rloc[j]] += 1
            rloc[newpos+1:pos+1], rloc[newpos] = rloc[newpos:pos], rloc[pos]
    print(list(B))
    #print(f'loc={loc}\nrloc={rloc} {"ok" if all([B[j] == A[rloc[j]] for j in range(N)]) else "!"} {"ok" if all([A[j] == B[loc[j]] for j in range(N)]) else "!"} B[4]={B[4]} rloc[4]={rloc[4]}')
i = list(B).index(0)
ans = sum([B[(i+k*1000)%N] for k in range(1,4)])
print(ans)
