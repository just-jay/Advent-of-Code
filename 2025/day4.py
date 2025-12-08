class Solution():
	
	def checkNeighbors(self,grid,i,j,rolls):
		count = 0
		if grid[i][j] == ".":
			return 0
		else:

			if i-1 >=0 and j-1 >= 0: #1
				if grid[i-1][j-1] == "@":
					count += 1
			if i-1 >= 0: #2
				if grid[i-1][j] == "@":
					count += 1
			if i-1 >= 0 and j+1 < len(grid[i]): #3
				if grid[i-1][j+1] == "@":
					count += 1
			if j+1 < len(grid[i]): #4
				if grid[i][j+1] == "@":
					count += 1
			if i+1 < len(grid) and j+1 < len(grid[i]): #5
				if grid[i+1][j+1] == "@":
					count += 1
			if i+1 < len(grid): #6
				if grid[i+1][j] == "@":
					count += 1
			if i+1 < len(grid) and j-1 >= 0: #7
				if grid[i+1][j-1] == "@":
					count += 1
			if j-1 >= 0: #8
				if grid[i][j-1] == "@":
					count += 1

		if count < 4:
			rolls.add((i,j))
			return 1
		else:
			return 0

	def part1(self):		
		grid = []
		rolls = set()
		with open("input4.txt") as f:

		#make a 2d array for the whole grid
			for l in f:
				row = []
				line = l.strip()
				for i in line:
					row += [i]
				grid.append(row)

		adjacencies = 0
		for i in range(0,len(grid)):
			for j in range(0,len(grid[i])):
				# print("curr",i,j)
				adjacencies += self.checkNeighbors(grid,i,j,rolls)

		print(adjacencies)


	def part2(self):
		grid = []
		rolls = set()
		totalAdjacencies = 0
		with open("input4.txt") as f:

		#make a 2d array for the whole grid
			for l in f:
				row = []
				line = l.strip()
				for i in line:
					row += [i]
				grid.append(row)

		#new part - while loop. Every time we can remove at least 1 roll, check the grid again 
		loopAgain = True
		while loopAgain:
			adjacencies = 0
			for i in range(0,len(grid)):
				for j in range(0,len(grid[i])):
					adjacencies += self.checkNeighbors(grid,i,j,rolls)
			
			totalAdjacencies += adjacencies
			for r in rolls:
				grid[r[0]][r[1]] = "."
			
			if adjacencies == 0: #if we found no rolls to remove, we can exit the loop 
				loopAgain = False
		print(totalAdjacencies)


if __name__ == "__main__":
	s = Solution()
	s.part1()
	s.part2()