# This code is based on the early video tutorial from the person who wrote "Automate the boring stuff"
# It firsts prompts for your name
# Then greets you and tells you how many letters are in the name you typed - less white space (I looked this up on stackoverflow)
# Then - originally it just asked for your age and printed out how old you will be next year 
# But my son, whom I was trying to impress with a wee program, entered 'no' for the age and the program broke out
# So I checked out how to check if the person entered an int and if they didn't, keep asking until they do

print ("Hello ! What is your name?")
YourName = input()
print ("Hi there " + YourName)
print ("There are " + str(len(YourName.replace(" ", ""))) + " letters, excluding white space, in your name")
TellingTheTruth = 0
while TellingTheTruth == 0:
    print ("I'm super nosey, how old are you?")
    try:
        YourAge = int(input())
        TellingTheTruth = 1
    except:
        print("Oh! Trying to trick me. I asked for your age")
        continue
print ("Wow, so you will be " + str(int(YourAge) +1) + " next year")

