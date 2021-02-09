#
# Create a program that puts 10 random numbers into a queue(list), the
# program should then output all the values in the queue, then take the
# numbers from the queue one at a time, print it and the current numbers still
# in the queue. (the command pop(0) takes the first element out of a list)
# 
# Based on Lab week 3, section 4 - Lists & Tuples

import random

tenRandomNumbers = []
numNums = 10
maxPossibleValues = 100

for number in range (0, numNums) :
    tenRandomNumbers.append(random.randint(0, maxPossibleValues))
	
print ("The 10 random numbers stored are {}".format(tenRandomNumbers))

while len(tenRandomNumbers) != 0:
    currentNumber = tenRandomNumbers.pop(0)
    print ("The current Number is {} and the remaining numbers in the queue are {} ".format(currentNumber, tenRandomNumbers))
print ("The queue 'tenRandomNumbers' is now empty")
