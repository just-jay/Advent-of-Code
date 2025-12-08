import copy

def _valid(nums, value,currSum):	
	if nums == []:
		return True if value == currSum else False
	A = nums[0]
	return _valid(nums[1:],value,currSum+A) or _valid(nums[1:],value,currSum*A)  


f = open("input7","r")
lines = f.readlines()
total = 0

for l in lines:
	l = l.strip()
	spl = l.split(": ")
	value = int(spl[0])
	nums = list(map(int, spl[1].split(" ")))

	A = nums[0]
	B = nums[1]
	add = A+B
	times = A*B

	if _valid(nums[2:],value,add) or _valid(nums[2:],value,times) :
		total += value

print(total)	