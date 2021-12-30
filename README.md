# GMIT CyberSecurity : Programming for CyberSecurity, Python
##                      End of term project submission
### Lecturer : Andrew Beatty ###
### Student  : Adele Harrington ###
### **Program Name :** idpghvul.py (Identify potential git hub vulnerabilities) ###
### **Current Status :** Work in progress ###
### **Program Function :** ###
       This program will
       * display a menu with the following options
           * Enter one or more org names
           * Enter one or more users
           * Enter an id range to be scanned
               if no id range is supplied use default & proceed
               For range option do simple checks such as min < max, min & max are both positive 
           * Collate orgs, users in orgs, users and users identified with range ids - remove duplicates
           * Get the associated repos, check the commits for vulerabilities (WIP)
             Note :  if no information is supplied use default !!! 
               * For each listed user
                   * download user respository to a temp directory
                   * check to see if the files downloaded have any obvious vulnerabilties such as passwords or keys
                   * record vulnerabilties
                   * remove tmp downloaded dir in preparation for next iteration
###**        Fun Add On :**###
             Every terminal run program needs an ascii text name that makes it look like an 80s arcade game title
###**Issues Encountered :**###
       This program has the potential to generate a lot of output so I really wanted something that would log informational messages versus actual potential problems
       separately. I opted to do two things
           1. Print the output in different colours
           2. Dual log - with everything going to the screen but potential problems being logged to one log file and purely informational stuff in a second file
           but .. I found that the method I used to change colours for the screen logging didn't translate in to the log file - if you vi the file it will contain the codes to 
           display the colours if the file is streamed to the terminal but the file itself will only be one colour. This was disappointing but I couldn't find a way around it.
###**References :**###
       1. [Pygithub Introduction] (https://pygithub.readthedocs.io/en/latest/introduction.html)
       2. [Generating temp files using Python] (https://www.tutorialspoint.com/generate-temporary-files-and-directories-using-python)
       3. [Python shutil for directory manipulation] (https://docs.python.org/3/library/shutil.html)
       4. [Python Regular Expressions] (https://www.programiz.com/python-programming/regex )
       5. [StackOverflow - Resolving GitHub errors] (https://stackoverflow.com/questions/9617336/how-to-resolve-git-did-not-exit-cleanly-exit-code-128-error-on-tortoisegit)
       6. [StackOverflow - Colour terminal text] (https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal)
       7. [Python Logging] (https://docs.python.org/3/library/logging.html )
       8. [Python - Multiple file logging] (https://stackoverflow.com/questions/11232230/logging-to-two-files-with-different-settings)
       9. https://www.w3schools.com/python/ref_func_set.asp
      10. [Fun Terminal Fonts] (https://towardsdatascience.com/prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b)
      11. [Python Command Line Arguments] (https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
###**Tracking additions/Changes asof Dec 17 2021 for git push comments**###
**17/12/2021**
       Modified idpghvul.py so that information scrolling to screen specifically mentioned info & vulnerabilitiy log file names. 
       Previously it just said "This file"
**20/12/2021**
       Not happy with the way the logging works at present. 
       Going to introduce command line arguments
           -h just a usage message explaining the program can be run in verbose mode or stealth mode - stealth will print errors only
           -s stealth mode will only log errors found
            verbose is useful for seeing what is happening and provides reassurance the program is running.
           - it will print messages for all files scanned not just the ones with errors 
            The programs default execution is verbose. If no parameter is passed the program will execute in verbose mode
            which is definitely provides reassurance the program is doing something
**30/12/2021**
       Read up on how to format a github .md file at [GitHub Docs] (https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)           
       Changed the logging to log to one output file. Stealth mode negates the need for two logs imo.
