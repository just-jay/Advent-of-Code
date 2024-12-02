import re

f = open("advent_file_1", "r")
lines = f.readlines()

sum = 0 

for l in lines:
	l = l.rstrip()
	nl = re.sub('[A-Za-z]','',l) #remove all letters
	a = int(nl[0]) * 10 # take first number
	b = 0

	if len(nl) == 1 : 
		b = int(nl[0]) # take first number again if theres only 1 
	else:
		b = int(nl[-1]) #else take last number 
	sum += a + b

print(sum)