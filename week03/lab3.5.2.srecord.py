# Lab 3.5.2
# 
# Write a program that stores and outputs a student's name, associated modules & grades
# At this time the information is hardcoded

Student =  {
    "Name" : "Adele",
    "EnrolledIn" : "CyberSecurity Cert Level 9",
    "Modules" : [
        { 
            "Subject" : "Cybersecurity IDR",
            "Grade"   : "TBD"
        },
        {
            "Subject" : "Programming Python",
            "Grade"   : "TBD"
        },
        {
            "Subject" : "Security Operations",
            "Grade"   : "TBD"
        }
    ]
}

print ("\n{} is enrolled in {} \n\n \t Subject \t Grade \n" .format(Student["Name"], Student["EnrolledIn"]))
for Module in Student["Modules"]:
    print("\t {} \t: {}".format(Module["Subject"], Module["Grade"]))
print ("\n")
    

