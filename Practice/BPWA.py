# The goal of this is to find the set that least fits so either one with no matches in other listed arrays or the one with te fewest matches
# My first attempt was in PWA.py and it only identified a set if it had nothing in common with others
# The sets are hardcoded -- I'm not sure yet how to take them as input
# There is no error checking on ensuring the types in each list set are the same or if the lists themselves are all the same length
# There is probably an easier way to do this but .. it actually took me about 12 hours to get this far CRINGE

import numpy as np
narray = np.array([['a','b','c','d'],['a','b','c','g'],['j','c','l','a'],['a','m','h','i'], ['x','z','a','b']])

numarrays = len(narray)
#print(numarrays)

ContainedIn = 0
Total = 0
Cur = 0 
CurIndex = -1

for i in range(numarrays):
	Total = 0
	for j in narray[i]:
		ContainedIn = 0

		for a in range(numarrays):
			if j in narray[a]:  
				ContainedIn +=1
				Total = Total + ContainedIn

	if Cur == 0:
		Cur = Total
	if Cur > Total :
		Cur = Total
		CurIndex = i

	#print (Total, narray[i])
				#print (j, narray[i], narray[a], ContainedIn)
					
print(narray[CurIndex])
