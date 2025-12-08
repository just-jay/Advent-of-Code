def _trail(grid,i,j,curr):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
		return 0
	if grid[i][j] != curr:
		return 0
	if curr == 9 and grid[i][j] == 9:
		return 1
	return _trail(grid,i-1,j,curr+1) + _trail(grid,i,j-1,curr+1) + _trail(grid,i+1,j,curr+1) + _trail(grid,i,j+1,curr+1)

grid = []
for l in open("input10"):
	l = l.strip()
	grid += [list(map(int,list(l)))]

total = 0
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] == 0:
			temp = _trail(grid,i,j,0)
			total += temp
print(total)