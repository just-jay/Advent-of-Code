import re
import math

#checks if all items in list end in Z
def allZ(l):
	for i in l:
		if not re.search("Z$", i):
			return False
	return True


f = open("advent_file_8","r")
lines = f.readlines()

instructions = lines.pop(0)
lines.pop(0) #remove whitespace

d = {}
for l in lines:
	s1 = l.strip().split("=")
	s2 = (s1[1].replace("(","")).replace(")","").split(",")

	d[s1[0].strip()] = [s2[0].strip(),s2[1].strip()]

# print(steps)
starts = []
for v in d.keys():
	temp = re.search("A$", v)
	if temp:
		starts.append(temp.string)

ends = []
for v in d.keys():
	temp = re.search("Z$", v)
	if temp:
		ends.append(temp.string)

nums = []

for curr in starts:
	i = 0
	steps = 0
	while curr not in ends:
		if i >= len(instructions)-1: #start over if you've looped around the instructions
			i = 0
		if instructions[i] == 'L':
			curr = d.get(curr)[0]
		else:
			curr = d.get(curr)[1]
		i+=1
		steps+=1
	nums.append(steps)

#caculate the least common multiple of all the numbers in the array 
def lcm(a,b):
	return ((a*b)/math.gcd(a,b))

val = int(nums.pop())

for i in nums:
	val = lcm(int(val), i)
print(val)