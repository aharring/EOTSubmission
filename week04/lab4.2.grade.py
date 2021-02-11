# Lab week 4. Focussing in conditional statements
# Write a program (grade.py) that reads in a students percentage mark and
# prints out corresponding the grade (the program should check that the
# percentage is valid:
# 	• Under 40% => Fail
# 	• Between 40% and 49% => Pass
# 	• Between 50% and 59% => Merit 2
# 	• Between 60% and 69% => Merit 1
# 	• Over 70% => Distinction
# Program modified to round up for .5+ 
# Program modified to continue to prompt for a grade until -1 is entered

percentage = 0

while percentage != -1 :

    percentage = round(float(input("Enter the percentage: ")))
    if percentage == -1 :
        break
    if percentage < 0 or percentage > 100:
        print ("Please enter a number between 0 and 100")
    elif percentage < 40: # we know it is greater than 0
        print ("Fail")
    elif percentage < 50: # between 40 and 49
        print ("Pass")
    elif percentage < 60: # between 50 and 59
        print ("Merit 1")
    elif percentage < 70: # between 60 and 69
        print ("Merit 2")
    else: # the only option left is between 70 and 100
        print ("Distinction")
