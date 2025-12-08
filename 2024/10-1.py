def _trail(grid,i,j,curr,ends):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
		return 0
	if grid[i][j] != curr:
		return 0
	if curr == 9 and grid[i][j] == 9:
		ends.add((i,j))
		return 1
	return _trail(grid,i-1,j,curr+1,ends) + _trail(grid,i,j-1,curr+1,ends) + _trail(grid,i+1,j,curr+1,ends) + _trail(grid,i,j+1,curr+1,ends)

grid = []
for l in open("input10"):
	l = l.strip()
	grid += [list(map(int,list(l)))]

total = 0
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] == 0:
			emptyset = set() #use a set to store the endpoints so you dont overcount
			_trail(grid,i,j,0,emptyset)
			total += len(emptyset)
print(total)