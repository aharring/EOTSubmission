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
#             Note :  if no information is supplied use default !!! 
#               . For each listed user
#                   . download user respository to a temp directory
#                   . check to see if the files downloaded have any obvious vulnerabilties such as passwords or keys
#                   . record vulnerabilties
#                   . remove tmp downloaded dir in preparation for next iteration
#         Fun Add On :
#             Every terminal run program needs an ascii text name that makes it look like an 80s arcade game title
#
# To Do :
#       Error handling needs to be better
#       Read about contributors. Now wondering if I have to include these
#       Might make words being tested for a passable file on the command line - probaly there are way more words and things I can think of.
#
# Issues Encountered :
#       This program has the potential to generate a lot of output so I really wanted something that would log informational messages versus actual potential problems
#       separately. I opted to do two things
#           1. Print the output in different colours
#           2. Dual log - with everything going to the screen but potential problems being logged to one log file and purely informational stuff in a second file
#           but .. I found that the method I used to change colours for the screen logging didn't translate in to the log file - if you vi the file it will contain the codes to 
#           display the colours if the file is streamed to the terminal but the file itself will only be one colour. This was disappointing but I couldn't find a way around it.
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

