# program : normalise.py, 
# Function :
#	1. Reads in a string 
#	2. Strips any leading
#	3. Or trailing spaces
#	4. Converts the string to lower case.
#	5. Outputs the length of the input and output strings.
#
# Sample of expected behaviour :
#	Please enter a string: Some StRiNg
#	That String normalised is :some string
#	We reduced the input string from 57 to 11 characters
#

stringForNormalisation = input("Please enter a string : ")
normalisedString = stringForNormalisation.strip().lower() # apply lower & left/right space stripping functions to inputted string

print ("\n\'{}\' normalised is \'{}\'" .format(stringForNormalisation, normalisedString))
print ("The input string length has been reduced from {} to {}" .format(len(stringForNormalisation), len(normalisedString)))

