# A student in the class tutorial asked how to pull out the middle sentence in 3 sentences using'.' as delimiters 
# This is my attempt
# I imagine it is a little flaky but it works for this example. 

import re
   
mystring = "I wonder.Will this work lets just add more letters. I hope so "

regex = "(?<=\.)[\s+\S+\s+]*(?=\.\s+)"
foundTextList = re.search(regex, mystring)
foundText = foundTextList
print(foundText[0])

