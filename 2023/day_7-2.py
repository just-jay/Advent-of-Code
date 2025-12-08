def handValue(map):
	v = list(map.values())
	v.sort()
	
	js = map.get('J',0)  # joker modifier

	if max(v) == 5: # 5 of a kind
		return 6 
	elif 4 in v: # 4 of a kind
		if js == 1 or js == 4: # if other card is a joker
			return 6 
		return 5
	elif 3 in v and 2 in v: # full house
		if js == 3 or js == 2: 
			return 6
		return 4 
	elif 3 in v: # 3 of a kind
		if js == 1 or js == 3: 
			return 5 
		return 3 
	elif v.count(2) == 2: #2 pairs
		if js == 2: # if jokers are one of the pairs
			return 5
		elif js == 1: 
			return 4
		return 2 
	elif v.count(2) == 1: #1 pair
		if js == 1 or js == 2:
			return 3
		return 1 
	else: #nothing
		if js == 1:
			return 1
		return 0

#convert 
def convertString(s):
	s = s.replace('J','a')
	s = s.replace('1','b')
	s = s.replace('2','c')
	s = s.replace('3','d')
	s = s.replace('4','e')
	s = s.replace('5','f')
	s = s.replace('6','g')
	s = s.replace('7','h')
	s = s.replace('8','i')
	s = s.replace('9','j')
	s = s.replace('T','k')
	s = s.replace('Q','l')
	s = s.replace('K','m')
	s = s.replace('A','n')
	return s

f = open("advent_file_7", "r") 
lines = f.readlines()

#seperate out the hands
h = []
for l in lines:
	l = l.strip().split(" ")
	
	# put each hand into a dict showing frequencies
	d = {}
	for i in l[0]:
		if i in d.keys():
			d[i] = d[i]+1
		else:
			d[i] = 1
	#caculate what each hand is
	v = handValue(d)

	#convert to all letters
	cs = convertString(l[0])
	h.append([v,[cs,l[0],l[1]]])

#sort all values 
h.sort()

ret = 0
for i in range (len(h)):
	ret += (int(h[i][1][2]) * int(i+1))

print(h)
print(ret)