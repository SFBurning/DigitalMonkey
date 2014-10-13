import re, sys, json

# Debug mode
debugMode = False 


def getFilePath(argv):
	return argv[1]


def parseLine(sourceFile):
	if debugMode:
		print "Starting"
	chapterPattern = re.compile("/(?<=-->)(.*\n*)*(?=-->)/")
	source = open(sourceFile, 'r')
	sourceText = source.read(10000)
	match = chapterPattern.match(sourceText)
	result = ""
	if match:
		result = match.group(0)
		print(result)
	print("match is " + str(match))

	testFile = open("intermediary.txt", "w")
	testFile.close()
	testFile = open("intermediary.txt", "a")
	json.dump(sourceText, testFile)
	outputFile = open("result.json", 'w')
	outputFile.close()
	outputFile = open("result.json", 'a')
	json.dump(result, outputFile)



sourceFile = getFilePath(sys.argv)

parseLine(sourceFile)