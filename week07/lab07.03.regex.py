# This is code will find some text in an access file
# Lab week07, point 3

import re
#regex = "GET .+\""
regex = "\[.*\]"
filename = "200linesaccess.log"

with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.search(r"\bGET", line)
        #if (len(foundTextList)!= 0):
        foundText = foundTextList
        print(foundTextList)
           # print(foundText[1:-1]) # Remove leading [ & trailing ]
