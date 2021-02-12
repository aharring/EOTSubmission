# Based on Lecture Week 4, Lab 2, point 7. 
# Write a program that reads in students until the user
# enters blank in they students first name. The program should then print
# the entire list of students

students = [] # Empty array

firstName =  input("\nEnter student's firstname (blank to quit): ").strip() # Prompt for firstname, strip spaces

while firstName != "": # Check loop entry condition
    student = {}  # Dict 
    student["firstName"] = firstName.capitalize() # Handy function found on w3schools. capitalizes first letter
    student["lastName"] = input("Enter student's lastname : ").strip().capitalize()
    students.append(student)
    firstName =  input("\nEnter student's firstname (blank to quit): ").strip() # Prompt for firstname, strip spaces


print ("\nHere are the student names you entered : \n" )
for currentStudent in students : # Loop through our array of dicts and print
    print ("\t\t {}{}" .format(currentStudent["firstName"],currentStudent["lastName"]))
print ("\n")

