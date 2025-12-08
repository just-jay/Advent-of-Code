class Solution():

	#geenrate each pair and return the largest
	def joltage(self,line):
		largest = 0
		for i in range(len(line)):
			for j in range(i+1,len(line)): #"brute force"
				temp = int(line[i] + line[j])
				if temp > largest:
					largest = temp
		return largest

	def joltageTwo(self,line):
		largestString = line[:12] #currentLargest 
		for i in range(12,len(line)):
			currElement = line[i]
			for i in range(12):
				temp = largestString[0:i] + largestString[i+1:12] + currElement
				if int(temp) > int(largestString):
					largestString = temp
					break
		return int(largestString)

	def part1(self):
		with open("input3.txt") as f:
			total = 0
			for line in f:
				l = line.strip()
				total += self.joltage(l)
		print(total)

	def part2(self):
		with open("input3.txt") as f:
			total = 0
			for line in f:
				l = line.strip()
				total += self.joltageTwo(l)
		print("total: " + str(total))


if __name__ == "__main__":
	s = Solution()
	# s.part1()
	s.part2()