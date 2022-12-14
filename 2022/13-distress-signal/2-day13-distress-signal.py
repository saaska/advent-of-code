"""## --- Part Two ---
Now, you just need to put *all* of the packets in the right order. Disregard the blank lines in your list of received packets.

The distress signal protocol also requires that you include two additional *divider packets*:
`[[2]]
[[6]]
`

Using the same rules as before, organize all packets - the ones in your list of received packets as well as the two divider packets - into the correct order.

For the example above, the result of putting the packets in the correct order is:
`[]
[[]]
[[[]]]
[1,1,3,1,1]
[1,1,5,1,1]
[[1],[2,3,4]]
[1,[2,[3,[4,[5,6,0]]]],8,9]
[1,[2,[3,[4,[5,6,7]]]],8,9]
[[1],4]
*[[2]]*
[3]
[[4,4],4,4]
[[4,4],4,4,4]
*[[6]]*
[7,7,7]
[7,7,7,7]
[[8,7,6]]
[9]
`

Afterward, locate the divider packets. To find the *decoder key* for this distress signal, you need to determine the indices of the two divider packets and multiply them together. (The first packet is at index 1, the second packet is at index 2, and so on.) In this example, the divider packets are *10th* and *14th*, and so the decoder key is `*140*`.

Organize all of the packets into the correct order. *What is the decoder key for the distress signal?*
"""
import sys, json
from functools import cmp_to_key

def ordered(a,b):
    # structural pattern matching, Python 3.10+
    match(a,b):
        case (int(x), int(y)):
            if x==y: return None
            return -1 if x < y else 1
        case (int(x), list(y)):
            return ordered([a], b)
        case (list(x), int(y)):
            return ordered(a, [b])
        case ([x, *rest1], [y, *rest2]):
            first_result = ordered(x, y)
            if first_result is not None: 
                return first_result
            else:
                return ordered(rest1, rest2)
        case ([], [y, *rest]):
            return -1
        case ([x, *rest], []):
            return 1

A = [json.loads(line) for line in open(0) if line !='\n'] + [[[2]], [[6]]]
A.sort(key=cmp_to_key(ordered))
print((A.index([[2]])+1) * (A.index([[6]])+1))

