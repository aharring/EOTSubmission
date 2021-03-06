# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
#
# Program Name : logger.py  
#

import sys
import logging # Term #1, Lecture 3, week 9

# The output from this program is very long/verbose
# The output will be split in to two files, one is purely informational & contains everything. The other contains details of suspicious entries only
# Ideally the informational messages will be streamed to stdout as well so that it is possible to see progress

debugLogFile = "idpghvul.log" # Just a straightforward log file
infoLogFile = "idpghvul.info" # This file will contain details of all repositories/files listed in commits as changed, as well as verification of keywords scanned

def configLogFile(name, log_file, level):

    handler = logging.FileHandler(log_file)
    stdout_handler = logging.StreamHandler(sys.stdout) # In addition to printing to the appropriate log file, output to the console

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)                         # File handler
    logger.addHandler(stdout_handler)                  # Output to stdout simultaneously - means I do no need a print in addition to logger command

    return logger


