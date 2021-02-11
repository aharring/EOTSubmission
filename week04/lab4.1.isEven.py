#  Labs Week 04. Looking at conditional statements
#
#  Write a program (isEven.py) that asks the user 
#  to enter in a number, and the
#  program will tell the user if the number is even or odd.

userInput = int(input("Please enter a number ")) # Prompt for input

if (userInput%2 == 0) :          # If the number divided by two has no remainder then it is even
    print (userInput, "is an even number \n")
else :
    print (userInput, "is an odd number \n")
