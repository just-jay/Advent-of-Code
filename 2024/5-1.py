f = open("input5","r")

chunks = f.read().split("\n\n")

rules = chunks[0].split()
manuals = chunks[1].split()

sum = 0

# print(rules)
# print(manuals)

#key:page, value: all numbers after that page
after = {}
for e in rules:
	parts = list(map(int,e.split("|")))
	if parts[0] in after:
		after[parts[0]] = after[parts[0]] + [parts[1]]
	else:
		after[parts[0]] = [parts[1]]


#key:page, value all numbers before that page
before = {}
for e in rules:
	parts = list(map(int,e.split("|")))
	if parts[1] in before:
		before[parts[1]] = before[parts[1]] + [parts[0]]
	else:
		before[parts[1]] = [parts[0]]

# print("afters", after)
# print("befores", before)

for i in manuals:
	nums = list(map(int,i.split(',')))

	valid = True

	#check each number to see if it follows the rules
	for j in range (0,len(nums)): 
		curr = nums[j]
		left = nums[:j]
		right = nums[j+1:]

		# print(curr)
		# print(left)
		# print(right)
		

		for e in left:
			# print("b",e in before[curr])
			if before.get(curr):
				valid = valid and (e in before[curr])

		for e in right:
			if after.get(curr):
				valid = valid and (e in after[curr])

	if valid:
		sum += nums[int(len(nums)//2)]

print(sum)
