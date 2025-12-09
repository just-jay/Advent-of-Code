class Solution():

	def part1(self):
		with open("input5.txt") as f:
			ranges = []
			fresh = []

			for line in f:
				line = line.strip()
				if "-" in line:
					l = line.split("-")
					ranges += [(int(l[0]),int(l[1]))]
				elif line == "":
					continue
				else: # line is a number / ingredient 
					curr = int(line)
					for r in ranges:
						if curr >= r[0] and curr <= r[1]:
							fresh += [curr]
							break

			print(len(fresh))

	def part2(self):
		ranges = []
		endpoints = []


		with open("input5.txt") as f:
			for line in f:
				line = line.strip()
				if "-" in line:
					l = line.split("-")
					endpoints += [(int(l[0]),int(l[1]))]

			endpoints.sort()

			for e in endpoints:	
				inserted = False
				for r in ranges:
					if int(e[0]) >= r[0] and int(e[1]) <= r[1]: #if we're a subset, break
						inserted = True
						break
					elif int(e[0]) < r[0] and int(e[1]) > r[1]: #superset
						ranges.pop()
						ranges += [((int(e[0]),int(e[1])))]
						inserted = True
						break
					elif int(e[0]) < r[0] and (int(e[1]) >= r[0] and int(e[1]) <= r[1]): #left overlap 
						ranges.pop()
						ranges += [((int(e[0]),int(r[1])))]
						inserted = True
						break
					elif int(e[1]) > r[1] and (int(e[0]) >= r[0] and int(e[0]) <= r[1]): #right overlap 
						ranges.pop()
						ranges += [((int(r[0]),int(e[1])))]
						inserted = True
						break

				if not inserted: #if its a distinct range, add it as a new range
					ranges += [((int(e[0]),int(e[1])))]

			#go through all the ranges and add up the sizes
			total = 0
			for r in ranges:
				total += (r[1]-r[0]+1)
			print(total)


if __name__ == "__main__":
	s = Solution()
	# s.part1()
	s.part2()