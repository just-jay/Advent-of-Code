import re

f = open("input3","r")

line = f.read().strip()
pairs = re.findall("mul\((\d+),(\d+)\)",line)

total = 0

for e in pairs:
	A = int(e[0])
	B = int(e[1])
	total += (A*B)

print(total)