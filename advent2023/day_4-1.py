import re
import math

f = open("advent_file_4","r")
lines = f.readlines()

sum = 0
for l in lines:
	m = re.search("Card\s+\d+:\s+(?P<card1>(\d+\s+)+)[|]\s+(?P<card2>(\d+\s+)+(\d+))",l)
	card1 = re.split("\s+",m.group('card1').strip())
	card2 = re.split("\s+",m.group('card2').strip())
	s = set(card1).intersection(set(card2))
	sum += math.pow(2,len(s)-1) if s else 0
print(int(sum))