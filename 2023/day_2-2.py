import re
import sys

#[red, green, blue]
def calculateTurn(r,c):
	for turn in r:
		if 'red' in turn:
			turn = re.sub('[a-z]','',turn)
			if int(turn) > c[0]:
				c[0] = int(turn)
		elif 'green' in turn:
			turn = re.sub('[a-z]','',turn)
			if int(turn) > c[1] :
				c[1] = int(turn)
		elif 'blue' in turn:
			turn = re.sub('[a-z]','',turn)
			if int(turn) > c[2]:
				c[2] = int(turn)
	return c

f = open("advent_file_2", "r")
lines = f.readlines()
result = 0
for l in lines:
	l = l[5:].strip().split(':')
	round = l[0]
	record = l[1].split(";")

	currMin = [0,0,0]
	for r in record:
		round = r.split(',')
		currMin = calculateTurn(round, currMin)
	
	print(currMin)
	result += (currMin[0]*currMin[1]*currMin[2])

print(result)