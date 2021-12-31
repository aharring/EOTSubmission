# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
# 
# Program Function :
#       This program will
#       . display a menu with the following options
#           . Enter one or more org names
#           . Enter one or more users
#           . Enter an id range to be scanned
#               if no id range is supplied use default & proceed
#               For range option do simple checks such as min < max, min & max are both positive. Review error checking* 
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
#       Might make words being tested for a passable file on the command line - probaly there are way more words and things I can think of.
#
# Issues Encountered :
#       This program has the potential to generate a lot of output so I really wanted something that would log informational messages versus actual potential problems
#       separately. I opted to do two things
#           1. Print the output in different colours
#           2. Dual log - with everything going to the screen but potential problems being logged to one log file and purely informational stuff in a second file
#           but .. I found that the method I used to change colours for the screen logging didn't translate in to the log file - if you vi the file it will contain the codes to 
#           display the colours if the file is streamed to the terminal but the file itself will only be one colour. This was disappointing but I couldn't find a way around it.
#           3. The dual log isn't really giving me the functionality I wanted. I had been hoping to avoid the use of regex to extract out items of interest since the output 
#              can be quite long but in hindsight a single logfile with options to run in stealth mode or verbose (default logging) is better
#
# References : 
#       1. https://pygithub.readthedocs.io/en/latest/introduction.html
#       2. https://www.tutorialspoint.com/generate-temporary-files-and-directories-using-python
#       3. https://docs.python.org/3/library/shutil.html
#       4. https://www.programiz.com/python-programming/regex 
#       5. https://stackoverflow.com/questions/9617336/how-to-resolve-git-did-not-exit-cleanly-exit-code-128-error-on-tortoisegit
#       6. https://docs.python.org/3/library/logging.html
#       7. https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations
#       8. https://www.kite.com/python/answers/how-to-print-logging-messages-to-both-stdout-and-to-a-file-in-python
#       9. https://www.w3schools.com/python/ref_func_set.asp
#      10. https://towardsdatascience.com/prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b 
#      11. https://www.tutorialspoint.com/python/python_command_line_arguments.htm
#      12. https://docs.python.org/3/howto/argparse.html#id1 .. more about command line arguments
#      13. https://docs.python.org/3/library/re.html
#      14. https://docs.python.org/3/library/tempfile.html
#      15. https://stackoverflow.com/questions/35972249/get-github-username-by-github-user-id
#      16. https://gitpython.readthedocs.io/en/stable/tutorial.html#meet-the-repo-type
#

import re       # Regular expression matching operations
import json
import shutil   # Allows directory operations such as rmdir
import logger   # Logging functionality separated out in to it's own module
import argparse # The program can be run in verbose mode with extensive logging or non verbose which doesn't log when it finds nothing
import pyfiglet # Ascii program banner
import requests # Http library 
import tempfile # This module allwos the creation of temporary files & directories
import subprocess # This is just to allow a clear screen for program execution

from git import Repo
from git import NULL_TREE

# Variable definitions & defaults

ghUrl = "https://api.github.com"

orgs = []
users = []
defaultUser = ['andrewbeattycourseware'] # default user in the event a scan is initiated without supplying an org or user or id

class colors:
    FILENAME = "\033[1;33m" # File name Bold Red
    COMMIT = "\033[1;36m"   # Commit name Bold Light Blue
    NORMAL = "\033[0m"
    WARNING = "\033[1;31m"  # WARNING keyword - Bold Red

# Keywords that might indicate vulnerabilities in a repository - this may go in to a configuration file that's read in
likelyCandidates = {
        "key",
        "API",
        "FTP",
        "MD5",
        "hash",
        "SHA-1",
        "SHA-2",
        "login",
        "secret",
        "random",
        "encrypt",
        "api_key",
        "password",
        "secret_key",
        "GitHub_token",
        "-----BEGIN PGP PRIVATE KEY BLOCK-----",
}

# Set up the log file that contains all execution output 
infoLog = logger.configLogFile('Execution Output', logger.infoLogFile, "INFO")

# Initial menu presented when program executes
# You can build your scan list by entering org names and/or users and/or id ranges
# The Scan is initiated only once when the user enters s.
# If no orgs/users/id ranges have been supplied then the default scan is for the lecturer, Andrew Beatty's, account

def displayMenu():

    print("What would you like to do?")
    print("\t(o) Enter github org name(s)")                               #
    print("\t(u) Enter github user account(s)")
    print("\t(i) Enter range of github ids")
    print("\t(s) Initiate scan & Exit. Default scan is for github user andrewbeattycourseware")
    print("\t(q) Do nothing. Exit.")
    selected = input("Type one letter (o/u/i/s/q):").strip()
    return selected

# displayMenu gives the option of entering org names for review.
# This function reads in the org names & stores them for processing
 
def readOrgNames():

    # I am not resetting orgs to [] here. This means as you jump around the menu orgs is added to each time you choose it

    org = input("\tEnter the Org name (blank to quit) :").strip()

    while org != "":
        orgs.append(org)
        # now read the next org
        org = input("\tEnter the Org name (blank to quit) :").strip()
    return orgs 

# displayMenu gives the option of entering user names for review.
# This function reads in the user names & stores them for processing
 
def readUserNames():

    # I am not resetting users to [] here. This means as you jump around the menu users is added to each time you choose it

    user = input("\tEnter the User name (blank to quit) :").strip()

    while user != "":
        users.append(user)
        # now read the next org
        user = input("\tEnter the User name (blank to quit) :").strip()
    return users 

# displayMenu gives the option of entering a range of ids associated with user accounts for review.
# This function reads in the min/max for range and stores them for processing
 
def readIDRange():
    rangeIDs = {} 
    rangeIDs["lower"]=int(input("\t\tEnter from id (int):"))
    rangeIDs["upper"]=int(input("\t\tEnter to id (int):"))
    return rangeIDs 

def cloneRepo(repoUrl):
# Make a tmp dir for repo getting health check
    tmpDir = tempfile.mkdtemp()
    Repo.clone_from(repoUrl, tmpDir)          # https://gitpython.readthedocs.io/en/stable/tutorial.html
    return tmpDir   

def requestRP(repoPath):
    repoPaths = requests.Response()
    try:
        repoPaths = requests.get(url=repoPath) # default query would execute a get on https://api.github.com/users/andrewbeattycourseware/repos
    except:
        pass
    return repoPaths.json()

#
# If an organisation is supplied instead or a user or id then we need to find all the users associated with the organisation
#
def idOrgUsers(orgs):

    resp = []
    for org in orgs:                                      # One or more orgs supplied by user input
        try:
            path = "{}/orgs/{}/members".format(ghUrl, org)
            resp = requestRP(path)
        except:
            pass
    for user in resp:
        try:
            users.append(user["login"])
        except:
            pass

#
# If given a range of ids try to find the associated github user names
# This function expects operates on the assumption the range is positive and min < max
#
def identifyUsersInRange (rangeIDs):

    lowerRId = rangeIDs["lower"]
    upperRId = rangeIDs["upper"]
    ids = range(lowerRId, upperRId)
    for id in ids:
        try:
            path = "{}/user/{}".format(ghUrl, id)
            resp = requestRP(path)
            users.append(resp["login"])
        except:
            pass
    return users # Again, I haven't reset users so the users list should be a culmination of all users/users in range/orgusers from menu hopping

def retrieveRepos ():
# Retrieving repos based on username. 
   
    # We might have to retrieve a combination of users from individual users, orgs and those supplied by range soooooo we need to make sure they are all included
    allUsers = orgs + users                                       # Haven't written range code yet 
    allUsers = set(allUsers)                                      # It seems possible to have duplicates so using python set should remove them

    if not allUsers :                                             # In the event no org/user/range was supplied
        allUsers = defaultUser

    for user in allUsers: 
        repoPath = "{}/users/{}/repos".format(ghUrl, user) 
        try: 
            listRepos = requestRP(repoPath) 
        except: 
            pass 
        for repo in listRepos: 
            if repo["fork"] == False :                 # If the repository is not a fork infoLog.info("Repo details\n%s", repo["git_url"])
                healthCheck(repo["git_url"]) 

def findPossibleProblems (commitDiff):

    if commitDiff.b_path != 'None' :
        if not args.stealth:
            infoLog.info("{}Checking {}{}{}" .format(colors.NORMAL, colors.FILENAME, commitDiff.b_path, colors.NORMAL))    # Messages streamed to the terminal will be coloured 

        blob_text = commitDiff.diff.decode("utf-8", errors="replace")
        for suspectPhrase in likelyCandidates:
            if re.search(suspectPhrase, blob_text, re.IGNORECASE):
                infoLog.info (
                    "{}Suspect phrase {} {} {} found in {} {} {}".format(
                        colors.NORMAL,
                        colors.WARNING,
                        suspectPhrase,
                        colors.NORMAL,
                        colors.COMMIT,
                        commitDiff.b_path,
                        colors.NORMAL
                    )
                )
            else :
                if not args.stealth:
                    infoLog.info("Suspect Phrase {} not found" .format(suspectPhrase))    # By default do extra logging because on first run it'll be helpful to know the program is running

def healthCheck(repoUrl):

    tmpDir = cloneRepo(repoUrl)           # Make a local copy of the gh url. 
    repo = Repo(tmpDir)
    branches = repo.remotes.origin.fetch()

    prevCommit = NULL_TREE
    infoLog.info("\nSearching Repo : {}" .format(repoUrl))

    for branch in branches:
        try:
            branchName = branch.name                                
        except:
            pass
        infoLog.info("BranchName : {}" .format(branchName))

        for commit in repo.iter_commits(branchName, max_count=50):
            infoLog.info(
                "\n==============================\n{}Searching commit {}{}{}".format(
                    colors.NORMAL, colors.COMMIT, commit.hexsha, colors.NORMAL
                )
             )

            if prevCommit == NULL_TREE :
                prevCommit = commit
            commitDiffs = commit.diff(prevCommit, create_patch=True)
            for commitDiff in commitDiffs:
                findPossibleProblems(commitDiff)
                prevCommit = commit

    # Remove tmpDir when done
    shutil.rmtree(tmpDir)
    return

#
# A number of options available to user for searches
#        A repo can be known by a users username or userid. Also, an organisation could have nuliple users associated with it
#        Present a menu option
#           1. Enter a github user name
#                  If the user is a valid github user retrieve the repos
#           2. Enter an organisation name
#                  If the organisation is valid, retrieve all users for that organisation
#           3. Every user has a numeric id associated with it. It's not necessary to know a users username
#                  For a range of ids return tha associated usernames  
#           4. it is possible to continue to add to the user list to be scanned by continuing to choose different menu options but
#                  a scan of the various repositories is only initiated if 's' is chosen. If 's' is chosen as the first option a default user account is scanned for words of interest

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--stealth", help="Dispense with logging messages where nothing is found",
                    action="store_true")
    args = parser.parse_args()

    subprocess.call('clear', shell=True)    # Found this when looking at port scanners. Thought it was nice

    selected = displayMenu()
    while(selected != 's'):
        if selected == 'o':                  
            orgs = readOrgNames()           # Read in then organisation names
            print (orgs)
            idOrgUsers(orgs)                # For each org in orgs - identify the users
        elif selected == 'u':
            users = readUserNames()         # Read in users 
        elif selected == 'i':
            rangeIDs = readIDRange()        # Just returns range
            users = identifyUsersInRange(rangeIDs) # Get all user names in the range supplied 
        elif selected == 'q':
            exit()
        elif selected !='s':
           print("\n\nplease select either o,u,i,s or q")
        selected=displayMenu()
      
# This code is only called once and it uses the built up list of users
 
    banner = pyfiglet.figlet_format("GHUB SCANNER")
    infoLog.info(banner)
    infoLog.info('{} file contains execution output' .format (logger.infoLogFile)) 
    retrieveRepos() 
