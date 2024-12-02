f = open("input2","r")

def _safeDiffer(arr):
	for i in range(len(arr)-1):
		elem = abs(int(arr[i])-int(arr[i+1]))
		if elem < 1 or elem > 3:
			return False
	return True

total = 0
for lines in f:
	curr = lines.strip().split(" ")
	for i in range(len(curr)):
		curr[i] = int(curr[i])

	for i in range(len(curr)):
		temp = list(curr) #make a new list here, need at least a shallow copy
		temp.pop(i)

		if (sorted(temp) == temp or sorted(temp, reverse=True) == temp) and _safeDiffer(temp):
			total += 1
			break
		
print(total)