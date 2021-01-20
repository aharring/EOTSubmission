# 20/01/2021 My first Python Program
# It imports the date module
# Then it create a variable 'today' and assigns todays date to it
# It then prints out a statement including todays date
# Then it uses the module subprocess to execute the command 'ls -alrt' 
# It assigns the returncode from executing the subprocess function run to completed
# It then prints the return code
# I am using W3schools to learn python syntax. I learned about the subprocess module from pymotw.com
# I tested this program by typing python3 firstprogram.py on my command line
# I am not sure yet how Anaconda is used with Python
# I've realised now that obviously running a subprocess means I have assumed the OS will run an ls command

from datetime import date

today = date.today()
print("I wrote my first python script:", today)

# Using module OS to get a directory listing
# I used listdir as opposed to walk because walk required a path but listdir lists the contents of the current directoy
import os
CurrentDirListing = os.listdir()
print("Printing the results of os.listdir command")
print(CurrentDirListing)

import subprocess
print("Executing subprocess command run with parameters ls -alrt")
commandreturncode = subprocess.run(['ls', '-alrt'])
print('returncode:', commandreturncode.returncode)
