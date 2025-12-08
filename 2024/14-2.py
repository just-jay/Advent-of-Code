'''

Had to get help with part 2 and look up solutions and heuristics
Even then I had to end up running someone elses solution to find the answer because my detection heuristic wasn't working
And then my code was having off by 1 errors to find the correct second/iteration 
All in all .. yeah not too proud of this one

'''


import re
from copy import deepcopy
import time

def _updateGrid(grid):
	newGrid = deepcopy(grid)
	for i in range(len(newGrid)):
		for j in range(len(newGrid[i])):
			newGrid[i][j] = []

	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] != []:
				robots = grid[y][x]

				while robots:
					e = robots.pop()
					newX = x + e[0]
					newY = y + e[1]
					# print(y,x,newY,newX,len(grid))

					if newX < 0:
						newX = len(grid[y]) +  newX

					if newY < 0:
						newY = len(grid) +  newY

					if newX >= len(grid[y]):
						newX = newX - len(grid[y])

					if newY >= len(grid):
						newY = newY - len(grid)

					# print(y,x,newY,newX,len(grid))

					newGrid[newY][newX].append(e)

	return newGrid



lines = open("input14").readlines()

grid = [] # each cell is an array that will hold all the robots at that position
for l in range(103):
	temp = []
	for j in range(101):
		temp.append([])
	grid.append(temp)

for l in lines:
	l = l.strip()
	point = re.search("p=(\d+),(\d+)",l)
	pX = int(point.group(2))
	pY = int(point.group(1))

	velocity = re.search("v=(-*)(\d+),(-*)(\d+)",l)
	vX = int(velocity.group(2))
	vY = int(velocity.group(4))

	if velocity.group(1) == "-":
		vX *= -1 
	if velocity.group(3) == "-":
		vY *= -1

	grid[pX][pY].append((vX,vY))

# for l in grid:
# 	print(l)
# print("\n")

currGrid = grid
for i in range(10000):
	currGrid = _updateGrid(currGrid)
	print(i)
	
	newGrid = []
	for l in currGrid:
		currStr = ""
		for e in l:
			if e == []:
				currStr += "."
			else:
				currStr += "1"
		newGrid += [currStr]
	
	todo = False
	for l in newGrid:
		if "111111" in l:
			todo = True
	if todo:
		for l in newGrid:
			print(l)
		print("\n")



#count the grid
'''
13
24
'''

# 1
count1 = 0
count2 = 0
count3 = 0
count4 = 0

for i in range(len(currGrid)//2):
	for j in range(len(currGrid[i])//2):
		if currGrid[i][j] != []:
			count1 += len(currGrid[i][j])

# 2
for i in range(len(currGrid)//2+1,len(currGrid)):
	for j in range(len(currGrid[i])//2):
		if currGrid[i][j] != []:
			count2 += len(currGrid[i][j])

# 3
for i in range(len(currGrid)//2):
	for j in range(len(currGrid[i])//2+1,len(currGrid[i])):
		if currGrid[i][j] != []:
			count3 += len(currGrid[i][j])

#4
for i in range(len(currGrid)//2+1,len(currGrid)):
	for j in range(len(currGrid[i])//2+1,len(currGrid[i])):
		if currGrid[i][j] != []:
			count4 += len(currGrid[i][j])

print(count1*count2*count3*count4)