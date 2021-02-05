# Program (randomGenerator.py) makes use of imported module random to print out a random number
# between  1 & 10
# Noted that randint expects parameter 1 to be less than param two  
# e.g. random.randint(10,1) will generate an error

import random

# Prompt for random range input. Assign to num1 & num2

num1 = int(input("Please enter a number :"))
num2 = int(input("Please enter a second number :"))
 
randomNum = random.randint(min(num1, num2),max(num1,num2))	# min & max used to ensure first param < second param
print ("Today's random number {}" .format(randomNum))
