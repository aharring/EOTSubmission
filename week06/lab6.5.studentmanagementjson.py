# Practicing using functions/modules
# Biggest issue still is with arrays and dicts, remembering {} versus [] and vice versa.
# This is week 05 tutorial labs with GMIT lecturer Andrew Beatty
# Modifying file week 06 to add a function to save the students infotmation to a json file
import json
import os

students =[]
filename = ("students.json")

def displayMenu():
    print("What would you like to do?")
    print("\t(l) Load from file?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save to file?")
    print("\t(q) Quit")
    choice = input("Type one letter (l/a/v/s/q):").strip()
    return choice

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()

    while moduleName != "":
        module = {}
        module["name"]= moduleName
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules

def displayModules (modules) :
    for module in modules :
        print("\t{}: {}" .format(module["name"], module["grade"]))
    print ("\n")

# New Code week 06 focussing on writing output to a json file
def doSave(students):
    with open(filename, "wt") as f :
        json.dump(students,f)

    print("\nSaved to file\n")

def readDict():
    print("\nLoading data\n")
    with open(filename) as f :
        return json.load(f) 

def doLoad(students):
    if os.path.exists(filename):
        students = readDict()
    else :
        print ("\nNo existing data\n")

    return students

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("Please enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

def doView(students):
    for currentStudent in students :
        print ("\nStudent Name : {}\n\tModule Grade\n" .format(currentStudent["name"]))
        displayModules(currentStudent["modules"])

def doNothing(dumby):
    pass

#the dict that maps a letter to function
#choiceMap = {
#    'a': doAdd,
#    'v': doView,
#    's': doSave,
#    'l': doLoad,
#    'q': doNothing # q is a valid choice
#}
#
#choice = displayMenu()
#while(choice != 'q'):
#    if choice in choiceMap:
#        # run the function
#        choiceMap[choice]( students)
#    else: # use did not enter something valid
#        print("\n\nplease select either a,v,s or q\n")
#    choice=displayMenu()

choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
       doAdd(students)
    elif choice == 'v':
       doView(students)
    elif choice == 's':
       doSave(students)
    elif choice == 'l':
       doLoad(students)
    elif choice !='q':
       print("\n\nplease select either l,a,v,s or q")
    choice=displayMenu()
