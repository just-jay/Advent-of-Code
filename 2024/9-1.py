
f = open("input9")
line = f.readline()
line.strip()

newline = []
currInt = 0

for i in range (len(line)):
	if i % 2 == 0:
		line[i]
		for i in range(int(line[i])):
			newline += [str(currInt)]
		currInt +=1 
	else:
		for i in range(int(line[i])):
			newline += ["."]


A = 0
B = len(newline)-1

newnewline = []

while A <= B:
	if newline[A] == ".":
		if newline[B] != ".":
			newnewline += [newline[B]]
			B -= 1
			A += 1
		else:
			B -= 1
	else:
		newnewline += [newline[A]]
		A += 1

for i in range(len(newline)-len(newnewline)):
	newnewline += ["."]


total = 0

for i in range(len(newnewline)):
	if newnewline[i] != ".":
		total += (i*int(newnewline[i]))
print(total)