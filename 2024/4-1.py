f = open("input4","r")
lines = f.readlines()

def _check(grid,i,j,word):
	
	temp = ""
	count = 0
	
	#check if the endpoint for each potential word exists
	NORTH = i-3 >= 0
	SOUTH = i+3 < len(grid)
	EAST = j+3 < len(grid[i])
	WEST = j-3 >= 0

	#N
	if NORTH:
		temp = grid[i][j] + grid[i-1][j] + grid[i-2][j] + grid[i-3][j]
		if temp == word:
			count+=1
	#NE
	if NORTH and EAST:
		temp = grid[i][j] + grid[i-1][j+1] + grid[i-2][j+2] + grid[i-3][j+3]
		if temp == word:
			count+=1
	#E
	if EAST:
		temp = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i][j+3]
		if temp == word:
			count+=1
	#SE
	if SOUTH and EAST:
		temp = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3]
		if temp == word:
			count+=1
	#S
	if SOUTH:
		temp = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j]
		if temp == word:
			count+=1
	#SW
	if SOUTH and WEST:
		temp = grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] + grid[i+3][j-3]
		if temp == word:
			count+=1
	#W
	if WEST:
		temp = grid[i][j] + grid[i][j-1] + grid[i][j-2] + grid[i][j-3]
		if temp == word:
			count+=1
	#NW
	if NORTH and WEST:
		temp = grid[i][j] + grid[i-1][j-1] + grid[i-2][j-2] + grid[i-3][j-3]
		if temp == word:
			count+=1
	
	return count


grid = []
for l in lines:
	curr = []
	for j in l.strip():
		curr.append(j)
	grid.append(curr)

count = 0
for i in range (len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == 'X': #semi-optimization 
			count += _check(grid,i,j,"XMAS")

print(count)
