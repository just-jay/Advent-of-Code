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
	if (sorted(curr) == curr or sorted(curr, reverse=True) == curr) and _safeDiffer(curr):
		total += 1
print(total)