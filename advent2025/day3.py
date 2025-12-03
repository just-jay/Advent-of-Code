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

		curr = line[:12]
		for i in range(12,len(line)):
			

			
		#idea at each number we either take or dont take
		#make all 12 possible values that could exist if we take 
		#be greedy? Take the largest one adn remove the numberX 


		return 0



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