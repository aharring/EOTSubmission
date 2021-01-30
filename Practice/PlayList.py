# Given an array of songs, of size n, 
# print you are playing the requested songnumber then place 
# it at the end of the queue and print the new queue
#

songqueue = ['A','B','C','D','E','F'] # Our pretend playlist
numsongs = len(songqueue) # The length of our playlist
inlist = 0 # A test condition variable

while inlist == 0:
	print ("Select song number") # Prompt for a songnumber
	# Make sure the user entered a number

	try :
		songnumber = int(input()) # Get the input from the user
	except :
		print ("Please enter the song number, not the song name")
		continue

	if songnumber <= numsongs: # Make sure that songnumber is in the range of songs available
		inlist = 1 # If it is, break out of the loop
	else:
		print ("Sorry, that song is not available") # otherwise tell the user it's not in range
							    # Stay in while loop

songname = songqueue[songnumber -1]
print ("Playing song number " + str(songnumber) + ", entitled " + str(songname))

songqueue = songqueue[:(songnumber-1)] + songqueue[songnumber:] 
songqueue.append(songname)

print ("New playlist " + str(songqueue) )
