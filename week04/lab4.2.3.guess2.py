# Lab week 4. Based on Lecture 2.
# Write a program (guess1.py) that prompts the user to guess a number, the
# program should keep prompting the user to guess the number until the user
# gets the right on
# Modify the program to tell if the guess is too high or too low
# Modify the program to generate a number between 0 and 100
#
import random

numberToGuess = random.randrange(0,100)
print (numberToGuess) # Printing the number for reference 

guess = int(input("Please guess the number:"))

while guess != numberToGuess:
    if guess < numberToGuess :
        guess = int(input("Your guess was too low. Please guess again: "))
    else :
        guess = int(input("Your guess was too high. Please guess again: "))

print ("Well done! Yes the number was ", numberToGuess)
