import re

def isValidRound(round):
	for turn in round:
		turn = turn.strip()
		if 'red' in turn:
			turn = re.sub('[a-z]','',turn)
			if int(turn) > 12:
				return False
		elif 'green' in turn:
			turn = re.sub('[a-z]','',turn)
			if int(turn) > 13:
				return False
		elif 'blue' in turn:
			turn = re.sub('[a-z]','',turn)
			if int(turn) > 14:
				return False
	return True

f = open("advent_file_2", "r")
lines = f.readlines()
sum = 0

for l in lines:
	l = l[5:].strip().split(':')
	num = l[0]
	record = l[1].split(";")
	result = True
	for r in record:
		#check if game was possible 
		round = r.split(',')
		result = result and isValidRound(round)
	if result:
		sum+=int(num)

print(sum)