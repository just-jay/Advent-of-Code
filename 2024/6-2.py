from copy import copy, deepcopy

def _gallivant(grid):
	gridCopy = deepcopy(grid)

	X = 0
	Y = 0

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == "^" or grid[i][j] == ">" or  grid[i][j] == "v" or grid[i][j] == "<":
				X = i
				Y = j


	direction = "N" # default start direction

	# get starting direction
	if grid[X][Y] == "^":
		direction = "N"
	elif grid[X][Y] == ">":
		direction = "E"
	elif grid[X][Y] == "v":
		direction = "S"
	elif grid[X][Y] == "<":
		direction = "W"

	count = 0
	validGrid = True
	while(True):
		gridCopy[X][Y] = 'X'

		# if you've passed the number of cells in the grid and are still looking at cells, you must be in a loop 
		# this is veryyy inefficient and took 2 minutes to run (but it works!)

		if(count > len(gridCopy) * len(gridCopy[X])):
			validGrid = False
			break

		if (direction == 'N' and X-1 < 0) or (direction == 'S' and X+1 > len(grid)-1) or (direction == 'W' and Y-1 < 0) or (direction == 'E' and Y+1 > len(grid[0])-1):
			break

	
		if direction == "N":
			if grid[X-1][Y] == "#":
				direction = "E"
				# print("turn East")
			else:
				X -= 1
		elif direction == "E":
			if grid[X][Y+1] == "#":
				direction = "S"
				# print("turn South")
			else:
				Y += 1
		elif direction == "S":
			if grid[X+1][Y] == "#":
				direction = "W"
				# print("turn West")
			else:
				X += 1
		elif direction == "W":
			if grid[X][Y-1] == "#":
				direction = "N"
				# print("turn North")
			else:
				Y -= 1
		count = count + 1
	return validGrid


f = open("input6","r")
grid = []
lines = f.readlines()

for l in lines:
	l = l.strip()
	temp = []
	for i in l:
		temp.append(i)
	grid.append(temp)

count = 0

for i in range(len(grid)):
	for j in range(len(grid[i])):
		temp = grid[i][j]
		grid[i][j] = "#"
		if not _gallivant(grid):
			count += 1
		grid[i][j] = temp

print(count)