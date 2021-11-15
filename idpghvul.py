# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
# 
#
# Program Name : idpghvul.py (Identify potential git hub vulnerabilities)
#
# Program Function : 
#	This program will 
#       . display a menu with the following options
#           . Enter one or more org names
#               if no org is supplied use default & proceed
#                   Not Written Yet
#           . Enter one or more users
#               if no user is supplied use default 
#               . For each listed user
#                   . download user respository to a temp directory 
#                   . check to see if the files downloaded have any obvious vulnerabilties such as passwords or keys
#                   . record vulnerabilties
#                   . remove tmp downloaded dir in preparation for next iteration
#           . Enter an id range to be scanned 
#               if no id range is supplied use default & proceed
#               For range option do simple checks such as min < max, min & max are both positive .. Not done yet
#                   Not Written Yet
#
# References : 
#       1. https://pygithub.readthedocs.io/en/latest/introduction.html
#       2. https://www.tutorialspoint.com/generate-temporary-files-and-directories-using-python
#       3. https://docs.python.org/3/library/shutil.html
#       4. https://www.programiz.com/python-programming/regex 
#       5. https://stackoverflow.com/questions/9617336/how-to-resolve-git-did-not-exit-cleanly-exit-code-128-error-on-tortoisegit
#       6. https://docs.python.org/3/library/logging.html
#       7. https://www.kite.com/python/answers/how-to-print-logging-messages-to-both-stdout-and-to-a-file-in-python
#

import re       
import json
import requests
import tempfile
import shutil
import logger   # Logging functionality separated out in to it's own module
#import logging # Term #1, Lecture 3, week 9

from git import Repo
from git import NULL_TREE

# Initial menu presented when program executes
def displayMenu():

    print("What would you like to do?")
    print("\t(o) Scan github organisation for potential vulnerabilities")
    print("\t(u) Scan github user account for potential vulnerabilities")
    print("\t(i) Scan user accounts associated with a range of github ids for potential vulnerabilities")
    print("\t(q) Quit")
    selected = input("Type one letter (o/u/i/q):").strip()
    return selected

# displayMenu gives the option of entering org names for review.
# This function reads in the org names & stores them for processing
 
def readOrgNames():
    orgs = []
    org = input("\tEnter the Org name (blank to quit) :").strip()

    while org != "":
        orgs.append(org)
        # now read the next org
        org = input("\tEnter the Org name (blank to quit) :").strip()
    return orgs 

# displayMenu gives the option of entering user names for review.
# This function reads in the user names & stores them for processing
 
def readUserNames():
    users = []
    user = input("\tEnter the User name (blank to quit) :").strip()

    while user != "":
        users.append(user)
        # now read the next org
        user = input("\tEnter the User name (blank to quit) :").strip()
    return users 

# displayMenu gives the option of entering a range of ids associated with user accounts for review.
# This function reads in the min/max for range and stores them for processing
 
def readIDRange():
    range = {} 
    range["lower"]=int(input("\t\tEnter from id (int):"))
    range["upper"]=int(input("\t\tEnter to id (int):"))
    return range 

# The output from this program is very long/verbose
# The output will be split in to two files, one is purely informational & contains everything. The other contains details of suspicious entries only
# Ideally the informational messages will be streamed to stdout as well so that it is possible to see progress
 
#debugLogFile = "idpghvul.log" # Just a straightforward log file, no timestamp, overwritten for each run
#infoLogFile = "idpghvul.info" # This file will contain details of all repositories/files listed in commits as changed, as well as verification of keywords scanned
#pVulLogFile = "idpghvul.pvul"

#def configLogFile(name, log_file, level):

#    handler = logging.FileHandler(log_file)        
#    stdout_handler = logging.StreamHandler(sys.stdout) # In addition to printing to the appropriate log file, output to the console
#
#    logger = logging.getLogger(name)
#    logger.setLevel(level)
#    logger.addHandler(handler)                         # File handler
#    logger.addHandler(stdout_handler)                  # Output to stdout simultaneously - means I do no need a print in addition to logger command
#
#    return logger

# Set up the log file that contains all execution output 
infoLog = logger.configLogFile('Execution Output', logger.infoLogFile, "INFO")
infoLog.info('This file contains complete execution output') 

# Set up the log file that contains details of suspicious keywords files found
pVulLog = logger.configLogFile('Potential Vulnerabilities', logger.pVulLogFile, "WARNING")
pVulLog.warning('This file contains suspect findings \n')

# Hardcoded for now.
users = ["andrewbeattycourseware"] # Just me for now
ghUrl = "https://api.github.com"

class colors:
    FILENAME = "\033[1;33m" # File name Bold Red
    COMMIT = "\033[1;36m"   # Commit name Bold Light Blue
    NORMAL = "\033[0m"
    WARNING = "\033[1;31m"  # WARNING keyword - Bold Red

# Keywords that might indicate vulnerabilities in a repository
likelyCandidates = {
        "key",
        "secret",
        "password",
        "encrypt",
        "API",
        "random",
        "hash",
        "MD5",
        "SHA-1",
        "SHA-2",
        "api_key",
        "secret_key",
        "FTP",
        "login",
        "GitHub_token",
        "-----BEGIN PGP PRIVATE KEY BLOCK-----",
}

def cloneRepo(repoUrl):
# Make a tmp dir for repo getting health check
    tmpDir = tempfile.mkdtemp()
    Repo.clone_from(repoUrl, tmpDir)
    return tmpDir   

def requestRP(repoPath):
    repoPaths = requests.Response()
    try:
        repoPaths = requests.get(url=repoPath)
    except:
        pass
    return repoPaths.json()

#
# If an organisation is supplied instead or a user or id then we need to find all the users associated with the organisation
#
def idOrgUsers():

    resp = []
    for org in orgs:                                      # One or more orgs supplied by user input
        try:
            path = "{}/orgs/{}/members".format(ghUrl, org)
            resp = requests_page(path)
        except:
            pass
    for user in resp:
        try:
            users.append(user["login"])
        except:
            pass

def retrieveRepos ():
# Retrieving repos based on username. Not concerned about orgs or contributors yet .. but will be
    for user in users:
        repoPath = "{}/users/{}/repos".format(ghUrl, user)
        listRepos = requestRP(repoPath)
    for repo in listRepos:
        if repo["fork"] == False :                                # If the repository is not a fork
            infoLog.info("Repo details\n%s", repo["git_url"])
            ###print (repo["git_url"])
            healthCheck(repo["git_url"])

def findPossibleProblems (commitDiff):

    infoLog.info("{}Checking {}{}{}" .format(colors.NORMAL, colors.FILENAME, commitDiff.b_path, colors.NORMAL))                    # Haven't quite figured out coloring text yet
    ######print("{}Checking {}{}{}".format(colors.NORMAL, colors.FILENAME, commitDiff.b_path, colors.NORMAL)) # Std Out - but ideally I don't want to have to write a separate line here

    blob_text = commitDiff.diff.decode("utf-8", errors="replace")
    for suspectPhrase in likelyCandidates:
        if re.search(suspectPhrase, blob_text, re.IGNORECASE):
            pVulLog.warning (
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
            ######print(
                ##"{}Suspect phrase {} {} {} found in {} {} {}".format(
                 ##   colors.NORMAL,
                  ##  colors.WARNING,
                   ## suspectPhrase,
                    ##colors.NORMAL,
                    ##colors.COMMIT,
                    ##commitDiff.b_path,
                    ##colors.NORMAL
                ##)
            ##)
        else :
            infoLog.info("Suspect Phrase {} not found" .format(suspectPhrase))
            ##print("Suspect Phrase {} not found" .format(suspectPhrase))

def healthCheck(repoUrl):

    tmpDir = cloneRepo(repoUrl)
    repo = Repo(tmpDir)
    branches = repo.remotes.origin.fetch()
    prevCommit = NULL_TREE
    # print (branches)        Just actually checking I've got something
    for branch in branches:
        branchName = branch.name
        infoLog.info(branchName)
    #    print("Branch name : {}" .format(branchName))
        for commit in repo.iter_commits(branchName, max_count=100):
            print("=" * 25)
            infoLog.info(
                "\n{}Searching commit {}{}{}".format(
                    colors.NORMAL, colors.COMMIT, commit.hexsha, colors.NORMAL
                )
            )

    #        print(
    #            "\n{}Searching commit {}{}{}".format(
    #                colors.NORMAL, colors.COMMIT, commit.hexsha, colors.NORMAL
    #            )
    #        )

            if prevCommit == NULL_TREE :
                prevCommit = commit
            commitDiffs = commit.diff(prevCommit, create_patch=True)
            for commitDiff in commitDiffs:
                findPossibleProblems(commitDiff)
            prevCommit = commit

    # Remove tmpDir when done
    shutil.rmtree(tmpDir)

#
# A number of options available to user for searches
#        A repo can be known by a users username or userid. Also, an organisation could have nuliple users associated with it
#        Present a menu option
#           1. Enter a github user name
#                  If the user is a valid github user retrieve the repos, scan commits for words/phrases of interest
#           2. Enter an organisation name
#                  If the organisation is valid, retrieve all users for that organisation then for each user, scan commits for words/phrases of interest
#           3. Every user has a numeric id associated with it. It's not necessary to know a users username
#                  For a range of ids return tha associated usernames, then for each user, scan commits for words/phrases of interest 

if __name__ == "__main__":
    selected = displayMenu()
    while(selected != 'q'):
        if selected == 'o':                 # 
            orgs = readOrgNames()
            print (orgs)
        elif selected == 'u':
            users = readUserNames()         # 
            print(users)
        elif selected == 'i':
            range = readIDRange()           # Basic, not finished
            print(range)
        elif selected !='q':
           print("\n\nplease select either o,u,i or q")
        selected=displayMenu()

        #retrieveRepos() Know this part works for users so just checking menu func
