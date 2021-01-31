# This program is based on Week 2 Labs  for programming for CyberSecurity, FirstPrograms.pdf 
# The labs were set by lecturer Andrew Beatty, GMIT
# This program satisfies steps 12 & 13 of FirstPrograms.pdf
#
# 12. Create a new file called hello2.py that reads in a person’s name and prints out
# hello that persons name
# 13. Modify to say nice to meet you after saying hello
#

# Prompt the user for their name
name = input("Please enter your name :")
print ("Hello {}\nNice to meet you!" .format(name))  # Without the space after the Hello the output would read Helloname where name is the input the user types

