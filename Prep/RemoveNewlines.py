import sys, re

filename = sys.argv[1]
def matchStrip():
	pass

f = open(filename, 'r')
outputFile = open("NoNewLines.txt", 'w')
extraSpaces = "{2,}\s"
for line in f:
	newLine = line.rstrip('\r\n,.;\'"!?')
	outputFile.write(newLine)
	re.sub("{2,}\s", " ", line)
outputFile.close()
f.close()