f = open("advent_file_6", "r") #note modified data to make it easier to read - kinda cheap but I am bad at parsing
lines = f.readlines()


def canBeat(a,r):
	curr = 0 
	for i in range (int(a)+1):
		dist = i * (int(a)-i)
		if dist > int(r):
			curr += 1
	if curr == 0:
		return 1
	else:
		return curr

val = 1 # assume we will win at least 1 race, makes math work better
for l in lines:
	l = l.split()

	#first is distance, second is time
	fin = canBeat(l[0],l[1])
	val *= fin
print(val)