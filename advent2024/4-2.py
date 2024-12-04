f = open("input4","r")
lines = f.readlines()

def _xmas(grid,i,j):
	if i > 0 and j > 0 and i < len(grid)-1 and j < len(grid[i])-1: # check for 'A' not being on an edge
		
		#check all surrounding cells for one of 4 valid cases

		'''
		########################
		M.S    S.S    S.M    M.M
		.A.    .A.    .A.    .A.
		M.S    M.M    S.M    S.S
		########################
		'''

		if grid[i-1][j-1] == 'M' == grid[i+1][j-1] and grid[i-1][j+1] == 'S' == grid[i+1][j+1]:
			return 1
		elif grid[i+1][j-1] == 'M' == grid[i+1][j+1] and grid[i-1][j-1] == 'S' == grid[i-1][j+1]:
			return 1
		elif grid[i-1][j+1] == 'M' == grid[i+1][j+1] and grid[i-1][j-1] == 'S' == grid[i+1][j-1]:
			return 1
		elif grid[i-1][j-1] == 'M' == grid[i-1][j+1] and grid[i+1][j-1] == 'S' == grid[i+1][j+1]:
			return 1

	return 0


grid = []
for l in lines:
	curr = []
	for j in l.strip():
		curr.append(j)
	grid.append(curr)

count = 0
for i in range (len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == 'A':
			count += _xmas(grid,i,j)

print(count)    