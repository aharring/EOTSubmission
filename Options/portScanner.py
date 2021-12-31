# Reading about port scanners so just running the basics to see what's happening.
# A break from the github code
# Very basic program - accepts a single hostname on the command line, 
#                      not so useful, better to have an ip address range
#                      also, wondering about timeouts since this works grand on a machine I know but when I try microsoft or hse it appears to stay on port 1

import sys
import socket
import subprocess
import pyfiglet # Ascii program banner. Learned this during exploration of GitHubScanner

from datetime import datetime

# Clear the screen - very handy. Will use in githubscanner n
subprocess.call('clear', shell=True)

# Display  a nice Banner 
banner = pyfiglet.figlet_format("PORT SCANNER") 
print (banner)

# Ask for input - obviously could use a config file too but let's just see things working first
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# And some information confirming the host being scanned 
print ("_" * 80)
print ("Please wait, scanning remote host", remoteServerIP)
print ("_" *80)

# Check the date and time the scan was started
t1 = datetime.now()

# Using the range function to specify ports
# Also we will do error handling

try:
    for port in range (1, 5000):
        print(port) # Just to be sure something is happening
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(20) #This is not doing what I hoped

        result = sock.connect_ex((remoteServerIP, port))

        if result == 0:
            print ("Port {}:        Open".format(port))
            sock.sendall(b'whoami')                  # The port is open - so .. send it something?
            data = sock.recv(1024)                   # ? Maybe it will send a reply?
            print (data)                             # Ever the optimist
            sock.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.timeout as timeout:
    print(timeout)
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

#Checking time again
t2 = datetime.now()

#Calculate the difference in time to now how long the scan took
total = t2 - t1

#Printing the information on the screen
print ('Scanning Completed in in ', total)

