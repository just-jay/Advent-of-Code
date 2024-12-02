import re

SPECIAL = ["!","@","#","$","%","^","&","-","+","=","*","/"]
NUMBER = ["1","2","3","4","5","6","7","8","9","0"]


# 1 2 3 
# 4 X 5
# 6 7 8

# if neighbor is a gear, return that gears index
def validate(table, i, j):
	if i-1 >= 0 and j-1 >=0: #1
		if lines[i-1][j-1] == "*":
			return (i-1,j-1)
	if i-1 >= 0: #2
		if lines[i-1][j] == "*":
			return (i-1,j)
	if i-1 >= 0 and j+1 <= len(table[i])-1: #3
		if lines[i-1][j+1] == "*":
			return (i-1,j+1)
	if j-1 >= 0: #4 
		if lines[i][j-1] == "*":
			return (i,j-1)
	if j+1 <= len(table[i])-1: #5
		if lines[i][j+1] == "*":
			return (i,j+1)
	if i+1 <= len(table)-1 and j-1 >= 0: #6
		if lines[i+1][j-1] == "*":
			return (i+1,j-1)
	if i+1 <= len(table)-1: #7
		if lines[i+1][j] == "*":
			return (i+1,j)
	if i+1 <= len(table)-1 and j+1 <= len(table[i])-1: #8
		if lines[i+1][j+1] == "*":
			return (i+1,j+1)

f = open("advent_file_3", "r")
lines = f.readlines()

#convert data into 2D array
table = []
for l in lines:
	l = l.strip()
	curr = []
	for c in l:
		curr.append(c)
	table.append(curr)

starDict = {}
for i in range (len(table)):
	head = False
	curr = ""
	starSet = set() #stores all stars next to the
	for j in range (len(table[i])):
		if table[i][j] in NUMBER: # if we're at a number
			temp = validate(table,i,j)
			if temp is not None:
				starSet.add(temp)
			curr += str(table[i][j])
			if not head: #if we haven't found the head of the number yet
				head = True
			#if we're at the end of the number or end of array (and have found the head)	
			if head and (j+1 == len(table[i]) or table[i][j+1] not in NUMBER): 				
				#add stars to dict
				for s in starSet:
					if s in starDict:
						l = starDict.get(s)
						l.append(curr)
						starDict[s] = l
					else:
						starDict[s] = [curr]
				head = False
				curr = ""
				starSet = set()
		else: # char is special or .
			continue
			
sum = 0
for k in starDict:
	v = starDict.get(k)
	if len(v) == 2:
		sum += (int(v[0])*int(v[1]))
print(sum)