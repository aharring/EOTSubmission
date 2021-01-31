# This program is based on Week 2 Labs  for programming for CyberSecurity, FirstPrograms.pdf 
# The labs were set by lecturer Andrew Beatty, GMIT
# This program satifies step 17 & 18 in the Extra section of FirstPrograms.pdf
#
# It firsts prompts for your name
# Then it prompts for your age
# Then it says hello and prints out how old you are
# It has simple error checking bc  my son, whom I was trying to impress with a wee program, entered 'no' for the age and the program broke out
# So I checked out how to check if the person entered an int and if they didn't, keep asking until they do
# I used w3schools to find the try/except syntax
#
# Included a second print statement to satisfy
# 	18. Modify the program so that it has a tab at the end of the name, (\t)

YourName = input("Hello ! What is your name?")
TellingTheTruth = 0

while TellingTheTruth == 0: # Make sure that the input received from prompt for age is indeed a number
    try:
        YourAge = int(input("How old are you?"))
        TellingTheTruth = 1 # This allows us to break out of the while loop - it means the condition above was satisfied
    except:
        print("Oh! Trying to trick me. I asked for your age") # Something other than a number was entered, stay in the loop, retry the try condition
        continue

print ("Hello {}, your age is " .format(YourName) + str(YourAge))
print ("Now printing with requested tab statement")

print ("Hello {},\t your age is " .format(YourName) + str(YourAge))


