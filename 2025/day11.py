class Solution():

	count = 0

	def helper(self,curr,visited,graph):
		if curr == "out":
			self.count += 1
			return 

		visited.add(curr)
		for v in graph[curr]:
			if v not in visited:
				self.helper(v,visited,graph) 
		visited.remove(curr)

	def part1(self):
		with open("input11.txt") as f:

			graph = {}
			for line in f:
				l = line.strip().split()
				l[0] = l[0].replace(":","")
				key = l.pop(0)
				graph[key] = l

			'''
			NOTE: can you do a DP algo here too? I think so
			'''

			self.helper("you",set(),graph)
			print(self.count)


if __name__ == "__main__":
	s = Solution()
	s.part1()	