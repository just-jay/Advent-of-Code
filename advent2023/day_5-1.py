import re

f = open("advent_file_5","r")
lines = f.readlines()


class AlmanacMap():
	def __init__(self,name,submap):
		self.name = name
		self.submap = submap

	def __str__(self):
		return f"Name:{self.name}, submap:{self.submap}"


seeds = []
middle = False #are we in the middle of fillign up a map
curr = []
mapName = ""
fullAlmanac = []
for l in lines:
	if l == "\n" and curr: #make new map
		fullAlmanac.append(AlmanacMap(mapName,curr))
		middle = False
		curr = []
		mapName = ""
	elif re.search("seeds",l):
		seeds = l.strip().replace("seeds: ","").split(" ")
	elif re.search("map:",l): #if you find a map name
		mapName = re.search("(\w+-\w+-\w+) map:",l).group(1)
		middle = True
	elif middle:
		curr.append(l.strip().split(" "))

print("Seeds: ",seeds)
for i in fullAlmanac:
	print(i)

# m = re.search("Card\s+\d+:\s+(?P<card1>(\d+\s+)+)[|]\s+(?P<card2>(\d+\s+)+(\d+))",l)
# card1 = re.split("\s+",m.group('card1').strip())