def handValue(map):
	v = list(map.values())
	v.sort()
	if max(v) == 5: # 5 
		return 6  
	elif 4 in v: # 4
		return 5
	elif 3 in v and 2 in v: # full house
		return 4
	elif 3 in v: # 3 
		return 3
	elif v.count(2) == 2: #2 pairs
		return 2
	elif v.count(2) == 1: #1 pair
		return 1
	else: #nothing
		return 0

#convert 
def convertString(s):
	s = s.replace('1','a')
	s = s.replace('2','b')
	s = s.replace('3','c')
	s = s.replace('4','d')
	s = s.replace('5','e')
	s = s.replace('6','f')
	s = s.replace('7','g')
	s = s.replace('8','h')
	s = s.replace('9','i')
	s = s.replace('T','j')
	s = s.replace('J','k')
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

	print(d)
	
	#convert to all letters
	cs = convertString(l[0])
	h.append([v,[cs,l[0],l[1]]])

#sort all values 
h.sort()

ret = 0
for i in range (len(h)):
	print(int(h[i][1][2]) * int(i+1))
	ret += (int(h[i][1][2]) * int(i+1))

print(h)
print(ret)