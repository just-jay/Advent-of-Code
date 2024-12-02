import re
import math

f = open("advent_file_4","r")
lines = f.readlines()

sum = 0
d = {} #card number : numbes of extras of that card we have
numCards = 0
for l in lines:
	m = re.search("Card\s+(?P<num>\d+):\s+(?P<card1>(\d+\s+)+)[|]\s+(?P<card2>(\d+\s+)+(\d+))",l)
	card1 = re.split("\s+",m.group('card1').strip())
	card2 = re.split("\s+",m.group('card2').strip())
	cardNumber = int(m.group('num'))
	s = set(card1).intersection(set(card2))

	nextCard = cardNumber + 1
	for e in s: #for the number of wins you've made
		if nextCard not in d: #if you've won a copy of the next card
			d[nextCard] = 1
		else:
			d[nextCard] = d.get(nextCard) + 1 
		nextCard += 1

	if cardNumber in d: #if the current card has copies, process them too
		for i in range(d.get(cardNumber)):
			nextCard = cardNumber + 1
			for e in s: #for the number of wins you've made
				d[nextCard] = d.get(nextCard) + 1 
				nextCard += 1
	numCards += 1
sum += numCards

for v in d.values():
	sum += v
print(sum)