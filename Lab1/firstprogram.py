# 20/01/2021 My first Python Program
# It imports the date module
# Then it create a variable 'today' and assigns todays date to it
# It then prints out a statement including todays date
# It then opens the ReadMe file and prints the contents to screen
# The ReadMe file explains what commands will run next - either listdir or ls -alrt, one uses os, one uses subprocees run
# The user is asked if they want to proceed
# If the user answers y or Y the code executes otherwise the program ends
# I am using W3schools to learn python syntax. I learned about the subprocess module from pymotw.com
# I tested this program by typing python3 firstprogram.py on my command line
# I am not sure yet how Anaconda is used with Python

from datetime import date

today = date.today()
print("Today is :", today)

ReadMe = open("ReadMe.txt", "r") 
# Open the file ReadMe.txt for reading
ReadMeContents = ReadMe.read() 
# Assign the contents of the file to the variable ReadMeContents
print (ReadMeContents) 
#Print the contents of the file now stored in variable ReadMeContents
ReadMe.close() 
# Close the file handle

UserInput = input("Continue y or n: ")
# Debug statement print("You entered: " + UserInput)

# Using module OS to get a directory listing
# I used listdir as opposed to walk because walk required a path but listdir lists the contents of the current directoy
if UserInput.upper() == "Y": 
	import os
	CurrentDirListing = os.listdir()
	print("Printing the results of os.listdir command")
	print(CurrentDirListing)

	import subprocess
	print("Executing subprocess command run with parameters ls -alrt")
	commandreturncode = subprocess.run(['ls', '-alrt'])
	print('returncode:', commandreturncode.returncode)
else:
	print("You chose not to execute the commands")
