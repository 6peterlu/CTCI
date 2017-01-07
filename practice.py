
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

#problem 1.2: check if one string is a permutation of another
def checkPermutation(strTup):
	str1 = strTup[0]
	str2 = strTup[1]
	return str1

def tester(testSet, correctSet, soln):
	for i in range(0, len(testSet)):
		test = testSet[i]
		result = soln(test)
		print ("Passed" if result == correctSet[i] else "Failed") + '	' + soln.__name__ +'("' + str(test) + '")=' + str(soln(test))

def main():
	testSet = [("cats", "stac"), ("aaaa", "aaaa"), ("hello", "yellow"), ("blaand", "alband"), ("rover", "overr")]
	correctSet = [True, True, False, True, True]
	tester(testSet, correctSet, checkPermutation)
main()