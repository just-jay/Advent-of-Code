import copy
def updateY(direction, y):
	if direction == "RIGHT":
		return y+1
	elif direction == "LEFT":
		return y-1
	else:
		return y

def updateX(direction, x):
	if direction == "UP":
		return x-1
	elif direction == "DOWN":
		return x+1
	else:
		return x

#/
def forwardSlash(direction):
	if direction == "UP":
		return "RIGHT"
	elif direction == "RIGHT":
		return "UP"
	elif direction == "DOWN":
		return "LEFT"
	elif direction == "LEFT":
		return "DOWN"

#\
def backSlash(direction):
	if direction == "UP":
		return "LEFT"
	elif direction == "LEFT":
		return "UP"
	elif direction == "DOWN":
		return "RIGHT"
	elif direction == "RIGHT":
		return "DOWN"

def move(x,y,direction,map,path):
	if x < 0 or x > len(map)-1 or y < 0 or y > len(map[0])-1:
		for l in path:
			temp[l[0]][l[1]] = "X"
		return 0 # out of bounds
	curr = map[x][y]
	print(path,(x,y,direction))
	if path.count((x,y,direction)) == 1:
		for l in path:
			temp[l[0]][l[1]] = "X"
		return 0 #in a cycle
	if curr == '.':
		path.append((x,y,direction))
		return 1 + move(updateX(direction, x),updateY(direction, y), direction, map,path)
	# elif curr == "|":
	# 	path.append((x,y,direction))
	# 	if direction == "UP" or direction == "DOWN":
	# 		return 1 + move(updateX(direction, x),updateY(direction, y), direction, map,path)
	# 	elif direction == "LEFT" or direction == 'RIGHT':
	# 		pathA = copy.deepcopy(path)
	# 		pathB = copy.deepcopy(path)
	# 		pathA.append((x,y,'UP'))
	# 		pathB.append((x,y,'DOWN'))
	# 		return 1 + move(updateX("UP", x),y, "UP", map,pathA) + move(updateX("DOWN", x),y, "DOWN", map,pathB)
	elif curr == "-":
		if direction == "LEFT" or direction == "RIGHT":
			path.append((x,y,direction))
			return 1 + move(updateX(direction, x),updateY(direction, y), direction, map,path)
		elif direction == "UP" or direction == "DOWN":
			pathA = copy.deepcopy(path)
			pathB = copy.deepcopy(path)
			pathA.append((x,y,'LEFT'))
			pathB.append((x,y,'RIGHT'))
			return 1 + move(x,updateY("LEFT", y), "LEFT", map,pathA) + move(x,updateY("RIGHT", y), "RIGHT", map,pathB)
	elif curr == "/":
		# print(path)
		newDirection = forwardSlash(direction)
		path.append((x,y,newDirection))
		return 1 + move(updateX(newDirection, x),updateY(newDirection, y), newDirection, map,path)
	elif curr == "\\":
		newDirection = backSlash(direction)
		path.append((x,y,newDirection))
		return 1 + move(updateX(newDirection, x),updateY(newDirection, y), newDirection, map,path)


f = open("advent_file_16","r")
lines = f.readlines()

map = []
for l in lines:
	l = l.strip()
	curr = []
	for c in l:
		curr.append(c)
	map.append(curr)


temp = copy.deepcopy(map)
currentPath = []

print(move(0,0,'RIGHT',map,currentPath))

for l in temp:
	c = ""
	for m in l:
		c += m
	print(c)
