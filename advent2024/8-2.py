import copy

grid = []

for l in open("input8"):
	temp = []
	for e in l.strip(): 
		temp.append(e)
	grid.append(temp)

d = {} #key = node letter or number, val = all nodes of that type as (x,y) coords

for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] != ".":
			if grid[i][j] in d:
				d[grid[i][j]].append((i,j))
			else:
				d[grid[i][j]] = [(i,j)]

gridCopy = copy.deepcopy(grid)

for i in d.keys():
	vals = d[i]
	for v in vals: #(v,w) is each pair of coords
		for w in vals:
			if v != w:
				#get slope between lines 
				M1 = v[0] - w[0] 
				M2 = v[1] - w[1]	

				X = v[0] 
				Y = v[1]
				while X >= 0 and X < len(gridCopy) and Y >= 0 and Y < len(gridCopy[0]):
					if gridCopy[X][Y] != "#": #this lets antinodes exist on antenna cells
						gridCopy[X][Y] = "#"
					X += M1
					Y += M2	

count = 0
for i in gridCopy:
	count += i.count("#")

print(count)