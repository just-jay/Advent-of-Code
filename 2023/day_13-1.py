f = open("advent_file_13","r")
lines = f.readlines()


# def validateVertical(a,b,pattern):
# 	return False

#make each column of the array 
def makeColumns(pattern):
	temp = []
	for i in range (len(pattern[0])):
		curr = ""
		for j in range (len(pattern)):
			curr+=(pattern[j][i])
		temp.append(curr)
		curr = ""
	return temp

def validateHorizontal(a,b,pattern):
	print(pattern)
	while a >=0 and b <= len(pattern):
		if pattern[a] != pattern[b]:
			return False
		a-=1
		b+=1
	return True

def horizontal(pattern):
	#find all possible lines of reflection
	for i in range (len(pattern)-1):
		if pattern[i] == pattern[i+1]:
			if validateHorizontal(i,i+1,pattern):
				return 100*(i+1)
	return 0

def reflectionValue (pattern):
	return horizontal(makeColumns(pattern))

currPattern = []
sum = 0 
for l in lines:
	if l == '\n':
		sum += reflectionValue(currPattern)
		currPattern = []
	else:
		l = l.strip()
		currPattern.append(l)
#need to do again for last pattern since file doesn't end in \n
sum += reflectionValue(currPattern) 
print(sum)