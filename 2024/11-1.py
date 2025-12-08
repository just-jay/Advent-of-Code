def _blink(stones):
	newStones = []
	for i in range (len(stones)):
		if stones[i] == 0:
			newStones.append(1)
		elif len(str(stones[i])) % 2 == 0:
			curr = str(stones[i])
			newStones.append(int(curr[0:len(curr)//2]))
			newStones.append(int(curr[len(curr)//2:len(curr)]))
		else:
			newStones.append(stones[i]*2024)

	return newStones


line = open("input11").readline().split(" ")
stones = list(map(int,line))


#go through line X amount of times
for i in range(25):
	stones = _blink(stones)
	print(stones)

print(len(stones))