# Lab week 6. Reading & writing files
#
# Write a program that outputs how many times it was run
# Store number of times program was run in count.txt
# If the file doesn't exist, create it and put a zero in it
# Read the number in the file. Increment the number by one. Print this number then write this number to the file 
# so that it is available for next execution
#
#
import os

filename = "count.txt"

def readNumber (filename) :
    with open (filename) as f:
        number = int(f.read())
        return number    

def writeNumber (numreads, filename) :
    with open (filename, "wt") as f :
        f.write(str(numreads))

if os.path.exists(filename):
    numreads = readNumber(filename)
    numreads += 1
else:
    with open (filename, "at") as f:
        f.write(str(0))

numreads = readNumber(filename)
numreads += 1
print ("We have run this program {} times".format(numreads))
writeNumber(numreads, filename)

