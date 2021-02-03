# This program prompts the user for their 
# Weight & Height then calculates their BMI
# and outputs the result

IsAFloat = False

# First prompt the user to enter their weight
# A simple check is done to see if the value entered evaluates to a float
# This is a basic check just to be sure the user didn't enter an alpha
# If the try condition succeeds then the program will exit the while loop
# Otherwise it will enter the exception and print the exception statement

while IsAFloat == False :
    print ("Please enter weight :")
    try :
        Weight = float(input())
        IsAFloat = True 
    except:
        print("Weight should be entered as a number ")
        continue

# Reset the test variable IsAFloat because we are now going to do a similar test
# on the Height input

IsAFloat = False

while IsAFloat == False :
    print ("Please enter height :")
    try :
        Height = float(input())
        IsAFloat = True 
    except:
        print("Height should be entered as a number ")
        continue

# Calculate the square of height & reassign it to the variable Height
Height = Height ** 2 
print (Height)

# Calculate the BMI
BMI = Weight/Height

# Print the BMI value
print ("Your BMI is " + str(BMI))

