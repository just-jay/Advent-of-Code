class Solution():

	def part1(self):
		with open("input9.txt") as f:
			coords = []
			for lines in f:
				l = lines.strip().split(",")
				coords += [(int(l[0]),int(l[1]))]

			value = 0
			for a in range(len(coords)):
				for b in range(a):
					temp = (abs(coords[a][0]-coords[b][0])+1)*(abs(coords[a][1]-coords[b][1])+1)
					if temp > value:
						value = temp
			print(value)

if __name__ == "__main__":
	s = Solution()
	s.part1()