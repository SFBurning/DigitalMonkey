import re, sys, json

# Debug mode
debugMode = False 


def getFilePath(argv):
	return argv[1]


def parseLine(sourceFile):
	if debugMode:
		print "Starting"
	chapterPattern = re.compile("(?<=-->)(.*\n*)*(?=-->)")
	source = open(sourceFile, 'r')
	sourceText = ""
	with open(sourceFile, "r") as myFile:
		sourceText = myFile.read().replace("\r","")
	result = chapterPattern.match(sourceText)
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