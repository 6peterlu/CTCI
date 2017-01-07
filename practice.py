
#problem 1.1: check if a string has all unique chararcters
def isUnique(inputStr):
	'''
	#naive soln: maintain a set of seen characters
	seen = []
	for i in range(0, len(inputStr)):
		if inputStr[i] in seen:
			return False
		seen.append(inputStr[i])
	return True
	'''

	#no extra data structures: sort string and then check adjacency
	sortedCharList = sorted(inputStr)
	for i in range(0, len(sortedCharList) - 1):
		if sortedCharList[i] == sortedCharList[i + 1]:
			return False
	return True

def isUniqueTest():
	testSet = ["hello", "abcde", "ijoeqpo", "aac", ""]
	correctSet = [False, True, False, False, True]
	for i in range(0, len(testSet)):
		test = testSet[i]
		result = isUnique(test)
		print ("Passed" if result == correctSet[i] else "Failed") + '	isUnique("' + test + '")=' + str(isUnique(test))

def main():
	isUniqueTest()
main()