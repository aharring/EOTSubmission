# Based on Lecture Week 4, Lab 2. For Loops
# Write a program (topthree.py) generates 10 random numbers (0-100) ,
# prints them out then prints out the top three.

import random

randomNumbers = []
numRandomNumbers = 10
topHowMany = 3

for i in range (0, numRandomNumbers) :
    randomNumbers.append(random.randrange(0, 100) )
print ("\n{} random numbers {} \t \n" .format(numRandomNumbers, randomNumbers))

randomNumbers.sort(reverse=True)
print ("\nThe top {} are {} ".format(topHowMany,randomNumbers[0:topHowMany]))


