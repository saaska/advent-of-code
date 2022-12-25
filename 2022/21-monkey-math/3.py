import sys, string, operator

def val(key):
    node = d[key]
    return node['value'] if 'value' in node else node['op'](*map(val,node['ops']))

getoper = {'*': operator.mul, '+': operator.add, '-': operator.sub, '/': lambda x, y: x/y}
d = {}
for line in open(0):
    name, *args = line.replace(':','').split()
    if args[0][0] in string.ascii_lowercase:
        d[name] = {'ops': args[0::2], 'op': getoper[args[1]]}
    else:
        d[name] = {'value': int(args[0])}

d['humn']['value'] = 3721298272960
print(val(d['root']['ops'][0]), val(d['root']['ops'][1]))
