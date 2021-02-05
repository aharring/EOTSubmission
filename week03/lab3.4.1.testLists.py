# Understanding lists
# Author: Adele Harrington, based on lecture & lab by lecturer Andrew Beatty
#

# demonstrating that a list can have hetrogenious types

anyList = [365,'forever', True]

# Since there are many functions for strings I thought there would be one for reverse.
# There is - you can work directly on the list but I made a copy

listCopy = anyList.copy()
listCopy.reverse()
print(anyList)
print(listCopy) 

# Print the original list, unmodified 

print ("\nUnmodified List \n")
for item in anyList:
    print(item )

# print reversed list using loop & reverse function

print ("Reversed list using reverse")
for item in listCopy:
    print(item )

print ("\nReversed List using ::1 method \n")

# print (anyList[::-1]) # Me checking what each piece of code does - this prints the List including []
print ('\n'.join(map(str,anyList[::-1])))

# a list of string
# aStringList=['asdf', 'hi', 'asdf']
# print('\n'.join(aStringList))
#
# but if the list has non string values in it
# then we will need to cast each item to a string
#print ('\n'.join(map(str,aList)))
