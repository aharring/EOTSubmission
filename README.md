# GMIT CyberSecurity : Programming for CyberSecurity, Python
#                      End of term project submission
#
# Lecturer : Andrew Beatty
# Student  : Adele Harrington
# 
#
# Program Name : idpghvul.py (Identify potential git hub vulnerabilities)
#
# Current Status : Work in progress
#
# Program Function :
#       This program will
#       . display a menu with the following options
#           . Enter one or more org names
#           . Enter one or more users
#           . Enter an id range to be scanned
#               if no id range is supplied use default & proceed
#               For range option do simple checks such as min < max, min & max are both positive .. Not done yet
#                   !!! Not Written Yet
#           . Collate orgs, users in orgs, users and users identified with range ids - remove duplicates
#           . Get the associated repos, check the commits for vulerabilities (WIP)
#             Note :  if no information is supplied use default !!! DONT FORGET TO DO THIS
#               . For each listed user
#                   . download user respository to a temp directory
#                   . check to see if the files downloaded have any obvious vulnerabilties such as passwords or keys
#                   . record vulnerabilties
#                   . remove tmp downloaded dir in preparation for next iteration
#
# To Do :
#       Error handling needs to be better
#       Read about contributors. Now wondering if I have to include these
#       Might make words being tested for a passable file on the command line - probbaly there are way more words and things I can think of.
#
# References : 
#       1. https://pygithub.readthedocs.io/en/latest/introduction.html
#       2. https://www.tutorialspoint.com/generate-temporary-files-and-directories-using-python
#       3. https://docs.python.org/3/library/shutil.html
#       4. https://www.programiz.com/python-programming/regex 
#       5. https://stackoverflow.com/questions/9617336/how-to-resolve-git-did-not-exit-cleanly-exit-code-128-error-on-tortoisegit
#       6. https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
#       7. https://docs.python.org/3/library/logging.html 
#       8. https://stackoverflow.com/questions/11232230/logging-to-two-files-with-different-settings
#       9. https://www.w3schools.com/python/ref_func_set.asp
#

