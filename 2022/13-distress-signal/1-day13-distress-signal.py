import sys, json

def ordered(a,b):
    # structural pattern matching, Python 3.10+
    match(a,b):
        case (int(x), int(y)):
            if x==y: return None
            return x < y
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
            return True
        case ([x, *rest], []):
            return False

line_num, ans = 0, 0
for pair in open(0).read().split('\n\n'):
    line_num += 1
    if ordered(*map(json.loads, pair.split('\n')[:2])):
        ans += line_num
print(ans)