from operator import itemgetter

f = open("input5","r")

chunks = f.read().split("\n\n")

rules = chunks[0].split()
manuals = chunks[1].split()

sum = 0

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

invalid = [] #invalid groups 

for i in manuals:
	nums = list(map(int,i.split(',')))

	valid = True

	#check each number to see if it follows the rules
	for j in range (0,len(nums)): 
		curr = nums[j]
		left = nums[:j]
		right = nums[j+1:]

		for e in left:
			if before.get(curr):
				valid = valid and (e in before[curr])

		for e in right:
			if after.get(curr):
				valid = valid and (e in after[curr])

##############
#  NEW CODE  #
##############

	if not valid:
		invalid.append(nums)

for line in invalid: # go through each invalid list 
	remaining = list(line) #make a list of all the remaining elements yet to be checked

	newlist = [] #new list with correct order
	for index in range(len(line)): #find the item that goes in the nth spot
		for elem in remaining: #consider each element 
			temp = list(remaining) #make a list from the remaining elements without for the current one
			temp.remove(elem)
			valid = True
			for e in temp:
				if e in before.get(elem): #if an element exists in the list that should go before the current one
					valid = False
			if valid:
				newlist.append(elem)
				remaining.remove(elem)

	sum += newlist[int(len(newlist)//2)]

print(sum)

			