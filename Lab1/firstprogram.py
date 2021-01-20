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

from datetime import date

today = date.today()
print("I wrote my first python script:", today)

import subprocess

commandreturncode = subprocess.run(['ls', '-alrt'])
print('returncode:', commandreturncode.returncode)
