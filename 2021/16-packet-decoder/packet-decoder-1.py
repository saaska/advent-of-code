children='C'
version= 'V'
parent=  'P'
opcode= 'Op'
value= 'Val'

vsum = 0

def parse(i, iend, nump, parentidx) -> int:
	global nodes, vsum
	if iend-i<6: return iend
	parsed_packets = 0

	# print(f'i:{i}, iend:{iend}, nump:{nump}, parentidx:{parentidx}')
	indent = ' '*i
	while i < iend and parsed_packets < nump:
		# print(' '+' '*i + s[i:])
		# print('['+' '*i +"VVVOOO", end='')
		p = nodes[parentidx]
		nodes.append( 
			{version: int(s[i:i+3], 2),
		      opcode: int(s[i+3:i+6], 2),
			  parent: parentidx})
		node, nodeidx = nodes[-1], len(nodes)-1
		p[children].append(nodeidx)
		if node[opcode] == 4:
			val = ''
			j = i+6
			while s[j]=='1':
				val += s[j+1:j+5]
				j += 5
				# print('l^^^^', end='')
			val += s[j+1:j+5]	
			j += 5
			# print('e^^^^'+' '*(iend-j)+']	')
			node[value] = int(val, 2)
		else:  # operator
			node[children] = []
			if s[i+6] == '0':  # know subpackets bitlength
				L = int(s[i+7:i+22],2)
				# print('L'+'b'*15 + 'v'*L+' '*(iend-i-22-L)+']')
				parse(i+22, i+22+L, 1000000, nodeidx)
				j = i+22+L
			else:              # know number of subpackets
				N = int(s[i+7:i+18],2)
				# print('N'+'-' + str(N) + '-'*(9-len(str(N)))+'>'+' '*(iend-i-18)+']')
				j = parse(i+18, iend, N, nodeidx)
		i = j
		vsum += node[version]
		parsed_packets += 1
		# print(f'{indent} iterend:{i}, packets parsed: {parsed_packets}')
	return i

nodes = [{children:[], parent:None, version:0}]
s = f'{int(input(),16):b}'
s = '0'*((4-len(s)%4)%4) + s
parse(0, len(s), 1, 0)
print(vsum)

# end: 2021-12-17T06:57:18Z
