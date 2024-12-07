def _valid(nums, value,currSum):
	if nums == []:
		return True if value == currSum else False
	return _valid(nums[1:],value,currSum+nums[0]) or _valid(nums[1:],value,currSum*nums[0]) or _valid(nums[1:],value,int(str(currSum)+str(nums[0]))) 


total = 0

for l in open("input7"):
	spl = l.strip().split(": ")

	value = int(spl[0])
	nums = list(map(int, spl[1].split(" ")))

	if _valid(nums[2:],value,nums[0]+nums[1]) or _valid(nums[2:],value,nums[0]*nums[1]) or _valid(nums[2:],value,int(str(nums[0])+str(nums[1]))):
		total += value

print(total)	
