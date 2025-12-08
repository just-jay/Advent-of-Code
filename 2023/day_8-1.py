f = open("advent_file_8","r")
lines = f.readlines()

instructions = lines.pop(0)
lines.pop(0) #remove whitespace

d = {}
for l in lines:
	s1 = l.strip().split("=")
	s2 = (s1[1].replace("(","")).replace(")","").split(",")

	d[s1[0].strip()] = [s2[0].strip(),s2[1].strip()]
print(d)

curr = "AAA"
i = 0
steps = 0
while curr != "ZZZ":
	if i >= len(instructions)-1: #start over if you've looped around the instructions
		i = 0
	if instructions[i] == 'L':
		curr = d.get(curr)[0]
	else:
		curr = d.get(curr)[1]
	i+=1
	steps+=1

print(steps)