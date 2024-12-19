globalVisited = None # 2D array of 0s

#all unvisited neighbors of the same type
def _getValidNeighbors(grid,i,j,visited):
	neighbors = []
		
	#North
	if grid[i-1][j] == grid[i][j]:
		neighbors.append((i-1,j))
	#East
	if grid[i][j+1] == grid[i][j]:
		neighbors.append((i,j+1))
	#South
	if grid[i+1][j] == grid[i][j]:
		neighbors.append((i+1,j))
	#West
	if grid[i][j-1] == grid[i][j]:
		neighbors.append((i,j-1))

	return neighbors

def _partialPerimeter(curr,e1,c,e2):
	numMatch = 0
	if curr == e1:
		numMatch += 1
	if curr == c:
		numMatch += 1
	if curr == e2:
		numMatch += 1

	if numMatch == 0:
		return 1
	elif numMatch == 1:
		return 1 if curr == c else 0
	elif numMatch == 2:
		 return 0 if curr == c else 1
	elif numMatch == 3:
		return 0



def _perimiterCalc(grid,i,j):
	val = 0
	'''
	+-+-+
	|1|2|
	+-X-+	the +'s are the spots we look at
	|4|3|
	+-+-+
	'''

	#1
	edge1 = grid[i][j-1]
	corner = grid[i-1][j-1]
	edge2 = grid[i-1][j]
	val += _partialPerimeter(grid[i][j],edge1,corner,edge2)

	#2
	edge1 = grid[i-1][j]
	corner = grid[i-1][j+1]
	edge2 = grid[i][j+1]
	val += _partialPerimeter(grid[i][j],edge1,corner,edge2)

	#3
	edge1 = grid[i][j+1]
	corner = grid[i+1][j+1]
	edge2 = grid[i+1][j]
	val += _partialPerimeter(grid[i][j],edge1,corner,edge2)

	#4
	edge1 = grid[i+1][j]
	corner = grid[i+1][j-1]
	edge2 = grid[i][j-1]
	val += _partialPerimeter(grid[i][j],edge1,corner,edge2)

	return val


def _BFS(grid,i,j):
	perimiter = 0
	
	queue = [(i,j)]
	globalVisited[i][j] = -1  
	visited = [(i,j)]

	while queue:
		curr = queue.pop(0)
		neighbors = _getValidNeighbors(grid,curr[0],curr[1],visited)
		
		# perimiter += 4 - len(neighbors)
		perimiter += _perimiterCalc(grid,curr[0],curr[1])
		
		for n in neighbors:
			if (n[0],n[1]) not in visited:
				globalVisited[n[0]][n[1]] = -1
				visited.append((n[0],n[1]))
				queue.append((n[0],n[1]))

	return perimiter * len(visited)



f = open("input12","r")
lines = f.readlines()
grid = []
dots = []

for l in lines:
	curr = ["."]
	for j in l.strip():
		curr.append(j)
	curr.append(".")
	grid.append(curr)

#surround the grid in a layer of dots to help with bound checking
for i in range(len(grid)+2):
	dots.append(".")
grid.insert(0,dots)
grid.append(dots)


globalVisited = []
for i in range(len(grid)):
	temp = []
	for j in range(len(grid[0])):
		temp.append(1)
	globalVisited.append(temp)

total = 0
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] != "." and globalVisited[i][j] == 1: #if curr has not been visited
			result = _BFS(grid,i,j)	
			total += result
print(total)


# for l in grid:
	# print(l)