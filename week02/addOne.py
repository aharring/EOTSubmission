# This program is based on Week 2 Labs  for programming for CyberSecurity, FirstPrograms.pdf 
# The labs were set by lecturer Adrew Beatty, GMIT
# This program satisfies step 14 of FirstPrograms.pdf
#
# Create a file called addOne.py, that reads in  a number and prints out one more
# than that number.

keeplooping = 1

# Simple error check to ensure that the value entered is indeed a number 
# Found the try except statement on w3schools
# The while loop ensure the test is repeated until a the try condition is met. Setting keeplooping to 0 breaks us out of the loop
while keeplooping:
	try :
		num = int(input("Please enter a number:"))	# variable 'num' stores int value of input 
		keeplooping = 0
	except:
		print ("Input must be a number")

num +=1	# Increment value in variable num by 1
print("{} is one greater than the number entered" .format(num))  # print out the new value
