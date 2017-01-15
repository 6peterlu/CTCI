from collections import deque
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
	#naive soln: sort both strings and compare
	return sorted(str1) == sorted(str2)
	#alternately, count the character frequencies in the strings as you go

#CURRENTLY DOESNT WORK
#problem 1.3: replace all spaces in string with %20
def URLify(inputTup):
	inputStr = list(inputTup[0])
	numChars = inputTup[1]
	charsCounted = 0
	curIndex = 0
	while(charsCounted < numChars):
		print curIndex
		examine = inputStr[curIndex]
		if examine == " ":
			del inputStr[-1]
			del inputStr[-1]
			del inputStr[curIndex]
			inputStr.insert(curIndex, "%")
			inputStr.insert(curIndex, "2")
			inputStr.insert(curIndex, "0")
			curIndex += 3
		else:
			charsCounted += 1
			curIndex += 1
	return "".join(inputStr)

#problem from Russell: reverse a linked list
def reverseDeque(dequeObj):
	localDeque = dequeObj
	newDequeObj = deque()
	newDequeObj.extendleft(localDeque)
	print newDequeObj
	return newDequeObj

def tester(testSet, correctSet, soln):
	for i in range(0, len(testSet)):
		test = testSet[i]
		result = soln(test)
		print ("Passed" if result == correctSet[i] else "Failed") + '	' + soln.__name__ +'("' + str(test) + '")=' + str(soln(test))

def main():
	testSet = [deque([1,2,3,4])]
	correctSet = [deque([4,3,2,1])]
	tester(testSet, correctSet, reverseDeque)
main()