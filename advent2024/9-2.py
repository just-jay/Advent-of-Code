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

#calculate the length of each chunk
#chunks holds a tuple of (the number, the length of the chunk, chunk's start index)
currChar = ""
currCharCount = 1
chunks = []

while A < len(newline):
	if newline[A] != ".":
		currChar = newline[A]
		if A+1 == len(newline) or newline[A+1] != currChar:
			chunks += [(int(currChar),int(currCharCount),A-int(currCharCount)+1)]
			A +=1
			currCharCount = 1
		else:
			currCharCount += 1
			A +=1
	else:
		A += 1

chunks.sort(reverse=True)


#for each chunk, iterate through newline. If you can insert it, insert it 
A = 0
B = len(newline)-1

for c in chunks:
	numDots = 0
	for i in range (c[2]):
		if newline[i] == ".":
			numDots += 1
			if numDots == c[1]:
				newline[i-c[1]+1:i+1] = [str(c[0])]*c[1] # replace the .. with the nums
				newline[c[2]:c[2]+c[1]] = ["."]*c[1] # replace the nums with ...
				break
		else: 
			numDots = 0

total = 0
for i in range(len(newline)):
	if newline[i] != ".":
		total += (i*int(newline[i]))
print(total)