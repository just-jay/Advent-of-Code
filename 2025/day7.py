
class Solution():

	'''
	index - tuple of current index
	chart - 2D array of grid
	visited - a set storing tuple sof all the visited nodes, so we dont double write any beams
	'''
	def helper(self,index,chart,visited):
		if index[0] > len(chart)-1 or index[1] < 0 or index[1] > len(chart[0]) - 1: #if we are out of bounds
			return 0

		if (index[0],index[1]) not in visited:
			visited.add((index[0],index[1])) # visit current
		else:
			return 0

		if chart[index[0]][index[1]] == "^":
			return 1 + self.helper((index[0],index[1]-1),chart,visited) + self.helper((index[0],index[1]+1),chart,visited)

		return self.helper((index[0]+1,index[1]),chart,visited)

	def part1(self):
		with open("input7.txt") as f:
			chart = []

			for lines in f:
				lines = lines.strip()
				curr = []
				for c in lines:
					curr += [c]
				chart += [curr]

			start = (0,chart[0].index("S")) #starting index 
			print(self.helper(start,chart,set()))

if __name__ == "__main__":
	s = Solution()
	s.part1()