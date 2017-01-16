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

#problem from Russell: convert number into word
def convertLessThanThousand(inputInt):
	oneDict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
	tensDict = {2:"twenty", 3:"thirty", 4:"fourty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
	teensDict = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
	outputString = ""
	if inputInt >= 100:
		outputString = outputString + oneDict[inputInt/100] + " hundred "
		inputInt = inputInt % 100
	if inputInt >= 20:
		outputString = outputString + tensDict[inputInt/10] + " "
		inputInt = inputInt % 10
	if inputInt >= 10:
		outputString = outputString + teensDict[inputInt] + " "
		inputInt = inputInt % 10
	if inputInt >= 1:
		outputString = outputString + oneDict[inputInt]
	return outputString
def convertNumberIntoWord(inputInt):
	outputString = ""
	if inputInt >= 1000:
		return convertLessThanThousand(inputInt/1000) + "thousand " + convertLessThanThousand(inputInt % 1000)
	else:
		return convertLessThanThousand(inputInt)


def tester(testSet, correctSet, soln):
	for i in range(0, len(testSet)):
		test = testSet[i]
		result = soln(test)
		print ("Passed" if result == correctSet[i] else "Failed") + '	' + soln.__name__ +'("' + str(test) + '")=' + str(soln(test))

def main():
	testSet = [456, 30986]
	correctSet = ["four hundred fifty six", "thirty thousand nine hundred eighty six"]
	tester(testSet, correctSet, convertNumberIntoWord)
main()