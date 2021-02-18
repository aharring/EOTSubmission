# Practicing using functions/modules
# Biggest issue still is with arrays and dicts, remembering {} versus [] and vice versa.
# This is week 05 tutorial labs with GMIT lecturer Andrew Beatty

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
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

students =[]

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
choiceMap = {
    'a': doAdd,
    'v': doView,
    'q': doNothing # q is a valid choice
}

choice = displayMenu()
while(choice != 'q'):
    if choice in choiceMap:
        # run the function
        choiceMap[choice]( students)
    else: # use did not enter something valid
        print("\n\nplease select either a,v or q\n")
    choice=displayMenu()
