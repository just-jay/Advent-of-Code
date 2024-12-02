f = open("input1","r")

A = []
B = []

for lines in f:
	curr = lines.strip().split("   ")
	A.append(int(curr[0]))
	B.append(int(curr[1]))

h = {}
for i in B: 
	if i in h: 
		h[i] = h[i]+1
	else: 
		h[i] = 1

total = 0 
for i in A: 
	if i not in h: 
		continue
	total += (i*h[i])

print(total)