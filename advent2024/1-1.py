f = open ("input1","r")

A = []
B = []

for lines in f:
	curr = lines.strip().split("   ")
	A.append(int(curr[0]))
	B.append(int(curr[1]))

A.sort()
B.sort()

total = 0

for i in range (len(A)):
	total += abs(A[i]-B[i])

print(total)