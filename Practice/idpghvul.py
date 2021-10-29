# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
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

import json
import requests
import tempfile
import shutil

from git import Repo

# Hardcoded for now.
users = ["aharring"] # Just me for now
ghUrl = "https://api.github.com"

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
        print (repoPath)
        listRepos = requestRP(repoPath)
    for repo in listRepos:
        if repo["fork"] == False:
            print (repo)
            healthCheck(repo["git_url"])

def findPossibleProblems ():
    print ("In findPossibleProblems")

def healthCheck(repoUrl):
    tmpDir = cloneRepo(repoUrl)
    print ("No idea how to step through clone lol")
    # Remove tmpDir when done
    shutil.rmtree(tmpDir)

if __name__ == "__main__":
    retrieveRepos()
