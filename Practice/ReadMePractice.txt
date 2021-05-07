# This is my python practice directory where I try test questions from various sources

# ATBSCh1.py is from AutomateTheBoringStuff - Chapter 1. It's based on getting input & writing output
# ATBSL3.py also from AutomateTheBoringStuff - Chapter 1 Introduces variable maniplation. Error checking learned from w3schools
# PWA.py is an earlier version of BPWA.py - all the comments are in BPWA.py. 2
# 	The goal of both is to find the set that least fits so either one with no matches in other listed arrays or the one with th fewest matches
# 	My first attempt was in PWA.py and it only identified a set if it had nothing in common with others
# 	I got the question from careercup, common google tech questions. I found it quite difficult
# PlayList.py is also based on a careercup question. 
# 	 Given an array of songs, of size n, 
# 	print you are playing the requested songnumber then place 
# 	it at the end of the queue and print the new queue
# PracticePlot.py
# 	Practice plotting a graph
# 	Based on the numpy module which I saw on w3schools
# pwfl.py
#	This program imports the subprocess module, runs a unix command from within the program and prints the output - it runs an ls
#
# sendmail.py 
#	This program only does a sendmail with smtp running in debug mode to the window
#	It doesn't actually send mail.  The command to smtp for python in debug mode is python -m smtpd -c DebuggingServer -n localhost:1025
#	I referenced an article on RealPython for details of how to start in debug mode
#
# sendmailSMTP_SSL.py WORKINPROGRESS - 
#	I set up the dummy email but thought rather than going with reduced security 
#	would attempt to set the account with added OAuth based on Google -
#	guides but even though everything seemed to install ok when I execute the program 
#	it fails and google tells me an account that is not trusted. Turns out if you enable Oauth then as a developer you have to
#	go through a verification process - which is not a simple click and you're done thing
#	Ok - removed the context statement & the ssl import - I think they may have been python2, lowered the security level for my
#	test account and it worked. Changed the program to prompt for both sender & 
#	recipients addresses as well as pw to avoid storing any info at all
#
# MaxNum.py This is working - but not if there are negative numbers in the array so needs fine tuning but was fun to write
#	The idea is that given an array of ints you are allowed use any combo of +-* to generate the largest possible number
#	so for example [1,1,1,5] would yield 15, while [1,3,4,5] would yield 80. This was another puzzle on careercup and at first it was very confusing
#	because in their example they gave of an input of [1,3,4,5] and said the highest number was 72 which I initially programmed for but - then I saw
#	you could get 80 - so I had another look at the logic and now I'm happier with it - just need to think a wee bit about handling negatives
#	
# CCArraySum.py
# 	Given an int array for element i create a new array with element i value plus the next i entries
# Iris4.py etcy 
#       Using Iris data file to practice lists/dicts, functions etc.
# EOD.py
#       So my 9 year old has expressed an interest in stocks - stocks if you don't mind! Anyway, I thought I'd use his interest in pennystocks
#       to my advantage and see if I could do a daily API call to get info for certain symbols - the free account only allows 1000 calls a month
#       and my guess is each symbol equates to one call - though I could be wrong. In any case I thought this might be a good learning experience for the whole
#       key and api thing .. Going to step through data analytics course a bit first
# FAB.py
#      Concept only at the mo - brother is doing DA course and has no coding buddy - well no one who will #      do any work so we're going to look at JCDecaux data and see what we can do with it - that's the brief     No code yet bc really need to look at the data

