class Solution():

	def partOne(self):
		dial = 50
		zeros = 0
		with open("input1.txt") as f:
			for l in f:
				cleanLine = l.strip()
				change = cleanLine[1:]
				
				if cleanLine[0] == "R":
					dial += int(change)
				else:
					dial -= int(change)

				dial = dial % 100

				if dial == 0:
					zeros+=1

		return(zeros)

	#solution with help from GPT
	#TLDR: Simulate each click 1 by 1 and update (no fancy math needed)
	def partTwo(self):
		dial = 50
		zeros = 0
		with open("input1.txt") as f:
			for l in f:
				cleanLine = l.strip()
				change = int(cleanLine[1:])

				for _ in range(change): #increment 1 by 1 adding the clicks
					if cleanLine[0] == "R":
						dial = (dial + 1) % 100
					else:
						dial = (dial - 1) % 100

					if dial == 0:
						zeros += 1
			return zeros


if __name__ == "__main__":
	s = Solution()
	# print(s.partOne())
	print(s.partTwo()) #6671