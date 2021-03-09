# This program reads in ile with regular expressions in it
# (which I have added some lines to because I wanted to double check the behaviour
# for each regular expression it goes through the quiz file and looks for matches
# The output is written to a file
 
import re
import os

filename = "quiz.txt"
inputFile = "regex.txt"
outputFile = "quizAnswers.txt"

if os.path.exists(outputFile): # remove output from previous run if it exists
    os.remove(outputFile)

def writeAns (regex, matchingLine, searchMatch, outputFile) :
    with open (outputFile, "at") as f :
        f.write("\nRegular Expression :" +  str(regex) + " Matching Line :" + matchingLine + " First Match " + searchMatch[0])

with open (inputFile, "rt") as inputRegexFile :
    for regex in inputRegexFile :
        regex = regex.strip("\n")
        with open (filename, "rt") as quizfile :
            searchResult = False
            for line in quizfile :
                print(regex + line)
                searchResult = re.search(regex, line)
                searchMatch = re.findall(regex, line)
                print(searchResult)
                if (searchResult) :
                    matchingLine = line
                    writeAns (regex, matchingLine, searchMatch[0], outputFile)
    
