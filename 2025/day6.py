class Solution():

	def part1(self):
		equations = []
		total = 0
		with open("input6.txt") as f:
			for lines in f:
				l = lines.strip().split()
				equations += [l]

			for i in range(len(equations[0])):
				operation = equations[len(equations)-1][i]

				if operation == "+":
					currTotal = 0
				else:
					currTotal = 1

				for j in range(len(equations)-1):
					if operation == "+":
						currTotal += int(equations[j][i])
					else:
						currTotal *= int(equations[j][i])
				total += currTotal
			print(total)

	def part2(self):

		rows = []
		total = 0
		with open("input6.txt") as f:
			for lines in f:
				rows += [lines]

		currOperation = "+"
		for i in range(len(rows[0])-1):
			currString = ""
			for j in range(len(rows)):
				currString += rows[j][i]

			#if theres a space, store the previous calculation
			if currString.isspace():
				total += currTotal
				continue	

			#set operation and current Total 
			if "+" in currString:
				operation = "+"
				currTotal = 0
				currString = currString.replace("+","")
			elif "*" in currString:
				operation = "*"
				currTotal = 1
				currString = currString.replace("*","")

			currString = currString.strip()

			if operation == "+":
				currTotal += int(currString)
			else:
				currTotal *= int(currString)

		total += currTotal # need to do the last calculation, since we only print it when we get to a space (and last line has no space)
		print(total)


if __name__ == "__main__":
	s = Solution()
	s.part1()
	s.part2()