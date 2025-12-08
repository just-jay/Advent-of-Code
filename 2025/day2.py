import re

class Solution():

	def checkBounds(self,a,b):
		val = 0
		for i in range(int(a),int(b)+1):
			length = len(str(i))
			if length % 2 == 0: #only even numbers count
				if str(i)[0:int(length/2)] == str(i)[int(length/2):length]: #split number in half, compare both sides
					val += i
		return val

	def checkBoundsPart2(self,a,b):
		val = 0
		for i in range(int(a),int(b)+1):
			temp = str(i)
			for j in range(int(len(temp))): #check every valid pattern we can make (this is suboptimal, we could cancel when were halfway)
				curr = temp[:j+1] #current pattern we're searching for 
				if curr != temp: #dont search for ourselves
					if len(temp) % len(str(curr)) == 0: #lengths match up to be a candidate for substrings
						if temp.count(curr) * len(curr) == len(temp): #if the length of pattern * number of occurences is the total length
							# print("string:" + str(temp) + " pattern:" + str(curr) + " count:" + str(temp.count(curr)))
							val += i
							break #dont need to keep checking if the ID is invalid
		return val

#NOTE: The functions take 5-10 seconds to complete on the given input 

	def partOne(self):
		with open("input2.txt") as f:
			lines = f.readline().split(",")

			total = 0
			for l in lines:
				bounds = l.split("-")
				total += self.checkBounds(bounds[0],bounds[1])
			print("total: " + str(total))

	def partTwo(self):
		with open("input2.txt") as f:
			lines = f.readline().split(",")

			total = 0
			for l in lines:
				bounds = l.split("-")
				total += self.checkBoundsPart2(bounds[0],bounds[1])
			print("total: " + str(total))


if __name__ == "__main__":
	s = Solution()
	# s.partOne()
	s.partTwo()