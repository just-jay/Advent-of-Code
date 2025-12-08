import re

f = open("input3","r")

line = f.read().strip()

do = True
count = 0

for i in range(len(line)):

	currLine = line[i:]

	if re.match("don't\(\)", currLine):
		do = False
	elif re.match("do\(\)", currLine):
		do = True

	if do:
		# print(currLine)
		elem = re.match("mul\((\d+),(\d+)\)",currLine)
		if elem:
			count += (int(elem.group(1))*int(elem.group(2)))

print(count)