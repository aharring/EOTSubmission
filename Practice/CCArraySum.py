# Given an Array A
# For every element in the array 
# Add a new entry to a new array that is made up of the element plus the values of the elements for the next ith entries.
#
# So for an array [3,4,7,9,2,8,6,11,12,13]
# The new array would be made as follows
# array[0] = 3 newarray = 3+contents of next 0 entries
# array[1] = 4 + 7
# array[2] = 7 + 9 + 2
# array[3] = 9 + 2 + 8 + 6
# array[4] = 2 + 8 + 6 + 11 + 12 
# array[5] = 8 + 6 + 11 + 12 + 13 .. end of array
# The sample output stopped calculating if the ith element was less than count i to the end
# 

inputArray = [3,6,2,7,9,5,4,1]
lenInputArray = len(inputArray)
outputArray = []

for arrayPos in range(lenInputArray) :
    toPos = (arrayPos*2) + 1
    if toPos > lenInputArray -1 :
        break
    outputArray.append(sum((inputArray[arrayPos:toPos])))
    arrayPos +=1

print (inputArray, outputArray)
