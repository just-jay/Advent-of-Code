globalVisited = None # 2D array of 0s

def _inBounds(grid,i,j):
	if i >= 0 and i < len(grid) and j >=0 and j < len(grid[0]):
		return True
	return False

#all unvisited neighbors of the same type
def _getValidNeighbors(grid,i,j,visited):
	neighbors = []
		
	#North
	if _inBounds(grid,i-1,j) and grid[i-1][j] == grid[i][j]:
		neighbors.append((i-1,j))
	#East
	if _inBounds(grid,i,j+1) and grid[i][j+1] == grid[i][j]:
		neighbors.append((i,j+1))
	#South
	if _inBounds(grid,i+1,j) and grid[i+1][j] == grid[i][j]:
		neighbors.append((i+1,j))
	#West
	if _inBounds(grid,i,j-1) and grid[i][j-1] == grid[i][j]:
		neighbors.append((i,j-1))

	return neighbors

def _BFS(grid,i,j):
	perimiter = 0
	
	queue = [(i,j)]
	globalVisited[i][j] = -1  
	visited = [(i,j)]

	while queue:
		curr = queue.pop(0)
		neighbors = _getValidNeighbors(grid,curr[0],curr[1],visited)
		#to count the perimiter, count the number of neighbors (NSEW) with the same letter, subtract that from 4.
		perimiter += 4 - len(neighbors)

		for n in neighbors:
			if (n[0],n[1]) not in visited:
				globalVisited[n[0]][n[1]] = -1
				visited.append((n[0],n[1]))
				queue.append((n[0],n[1]))

	return perimiter * len(visited)



f = open("input12","r")
lines = f.readlines()
grid = []

for l in lines:
	curr = []
	for j in l.strip():
		curr.append(j)
	grid.append(curr)

globalVisited = []
for i in range(len(grid)):
	temp = []
	for j in range(len(grid[0])):
		temp.append(1)
	globalVisited.append(temp)

total = 0
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if globalVisited[i][j] == 1: #if curr has not been visited
			result = _BFS(grid,i,j)	
			total += result
print(total)
