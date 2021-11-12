# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
# 
#
# Program Name : idpghvul.py (Identify potential git hub vulnerabilities)
#
# Program Function : 
#	Initially this program will 
#       1. download my respository to a temp directory 
#       2. check to see if the files downloaded have any obvious vulnerabilties such as passwords or keys
#       3. record vulnerabilties
#       4. remove tmp downloaded dir in preparation for next iteration
#
# References : 
#       1. https://pygithub.readthedocs.io/en/latest/introduction.html
#       2. https://www.tutorialspoint.com/generate-temporary-files-and-directories-using-python
#       3. https://docs.python.org/3/library/shutil.html
#       4. https://www.programiz.com/python-programming/regex 
#       5. https://stackoverflow.com/questions/9617336/how-to-resolve-git-did-not-exit-cleanly-exit-code-128-error-on-tortoisegit
#

import re       
import json
import requests
import tempfile
import shutil
import logging # Term #1, Lecture 3, week 9

from git import Repo
from git import NULL_TREE

# Redirecting Debug to output idpghvul.log
DEBUG_LOG_FILE = "idpghvul.log" # Just a straightforward log file, no timestamp, overwritten for each run

fileHandler = logging.FileHandler("{0}".format(DEBUG_LOG_FILE))
rootLogger = logging.getLogger()
rootLogger.addHandler(fileHandler)
rootLogger.setLevel(logging.DEBUG)             # Debug Level

# Hardcoded for now.
users = ["andrewbeattycourseware"] # Just me for now
ghUrl = "https://api.github.com"

class colors:
    FILENAME = "\033[1m"
    NORMAL = "\033[0m"
    WARNING = "\033[93m"

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

def retrieveRepos ():
# Retrieving repos based on username. Not concerned about orgs or contributors yet 
    for user in users:
        repoPath = "{}/users/{}/repos".format(ghUrl, user)
        logging.debug("Repo Path\n%s", repoPath)   # Logging repo path being reviewed
        listRepos = requestRP(repoPath)
    for repo in listRepos:
        if repo["fork"] == False :                                # If the repository is not a fork
            logging.info("Repo details\n%s", repo["git_url"])     # Logging repo path being reviewed
           #  print (repo)
            healthCheck(repo["git_url"])

def findPossibleProblems (commitDiff):

    logging.info("Checking {}{}{}\n".format(colors.FILENAME, commitDiff.b_path, colors.NORMAL)) 
    print("{}{}{}".format(colors.FILENAME, commitDiff.b_path, colors.NORMAL))
    blob_text = commitDiff.diff.decode("utf-8", errors="replace")
    for suspectPhrase in likelyCandidates:
        if re.search(suspectPhrase, blob_text, re.IGNORECASE):
            print(
                "Found suspectPhrase {}{}{} in this file. You should check if there are {}{} exposed.".format(
                    colors.WARNING,
                    suspectPhrase,
                    colors.NORMAL,
                    colors.WARNING,
                    colors.NORMAL,
                )
            )
        else :
            logging.info("Suspect Phrase {} not found" .format(suspectPhrase)) 

def healthCheck(repoUrl):

    logging.debug("In healthCheck : Param Repo Url = %s", repoUrl) 

    tmpDir = cloneRepo(repoUrl)
    repo = Repo(tmpDir)
    branches = repo.remotes.origin.fetch()
    prevCommit = NULL_TREE
    # print (branches)        Just actually checking I've got something
    for branch in branches:
        branchName = branch.name
        logging.info(branchName)
        print(branchName)
        for commit in repo.iter_commits(branchName, max_count=100):
            print("=" * 25)

            logging.info(
                "\n{}Searching commit {}.{}".format(
                    colors.FILENAME, commit.hexsha, colors.NORMAL
                )
            )

            print(
                "\n{}Searching commit {}.{}".format(
                    colors.FILENAME, commit.hexsha, colors.NORMAL
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

if __name__ == "__main__":
    retrieveRepos()
