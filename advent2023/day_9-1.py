def predict(line, prevline):
	if line.count(0) == len(line):
		return 0
	temp = []
	for i in range (len(line)-1):
		temp.append(int(line[i+1])-int(line[i]))
	return predict(temp,line) + line[len(line)-1]

f = open("advent_file_9", "r")
lines = f.readlines()

sum = 0 
for l in lines:
	curr = l.strip().split(' ')
	curr = list(map(int,curr)) # convert each str to ints
	for i in range (len(curr)): 
		curr[i] = int(curr[i])
	sum += predict(curr,[]) 
print(sum)