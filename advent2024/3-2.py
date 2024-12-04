import re

f = open("input3","r")

line = f.read().strip()
arr = line.split("do()") 


##############################
##     DOES NOT WORK YET    ##
##############################
newarr = []
for e in arr:
	newarr.append(re.sub("don't().*$","",e)) 

#rest is essentially the same as part1
pairs = []
for e in newarr:
	print(e)
	pairs.append(re.findall("mul\((\d+),(\d+)\)",e))

total = 0

for e in pairs:
	if e != []:
		A = int(e[0][0])
		B = int(e[0][1])
		total += (A*B)
		print(A,B, A*B)

print(total)