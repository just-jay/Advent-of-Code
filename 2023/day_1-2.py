import re

#if a number is spelled out at the given substring, return that number
#otherwise return -1
def isANumber(substring, index):
	sub = substring[index:]
	if sub.startswith("one"):
		return 1
	elif sub.startswith("two"):
		return 2
	elif sub.startswith("three"):
		return 3
	elif sub.startswith("four"):
		return 4
	elif sub.startswith("five"):
		return 5
	elif sub.startswith("six"):
		return 6
	elif sub.startswith("seven"):
		return 7
	elif sub.startswith("eight"):
		return 8
	elif sub.startswith("nine"):
		return 9
	else:
		return -1

#same as above but backwards
def isABackwardsNumber(substring, index):
	sub = substring[index:]
	if sub.startswith("eno"):
		return 1
	elif sub.startswith("owt"):
		return 2
	elif sub.startswith("eerht"):
		return 3
	elif sub.startswith("ruof"):
		return 4
	elif sub.startswith("evif"):
		return 5
	elif sub.startswith("xis"):
		return 6
	elif sub.startswith("neves"):
		return 7
	elif sub.startswith("thgie"):
		return 8
	elif sub.startswith("enin"):
		return 9
	else:
		return -1


f = open("advent_file_1", "r")
lines = f.readlines()

sum = 0 

a = 0;
# find first number
for l in lines:
	l = l.strip()
	for i in range(len(l)): 
		if l[i].isdigit() is True: #first real digit is a number
			a = int(l[i])
			break
		else: #first real digit MAY be a letter, we need to check
			if isANumber(l, i) != -1:
				a = isANumber(l, i)
				break
	sum += a*10

#find second number 
for l in lines:
	l = l.strip()
	l = l[::-1]
	for i in range(len(l)):
		if l[i].isdigit() is True: #first real digit is a number
			b = int(l[i])
			break
		else: #first real digit MAY be a letter, we need to check
			if isABackwardsNumber(l, i) != -1:
				b = isABackwardsNumber(l, i)
				break
	sum += b


print(sum)

"""
one
two three
four five
six seven
eight 
nine
"""