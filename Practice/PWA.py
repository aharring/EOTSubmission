
import numpy as np
narray = np.array([['a','b','c','d'],['a','b','c','g'],['j','p','l','a'],['a','b','h','i'], ['x','z','a','b']])

numarrays = len(narray)
#print(numarrays)

GTO = list()
NGTO = list()

ContainedIn = 0
AddToGTO = 0 
Added = 0
Total = 0
Cur = 0 
Culprit = list()
CurIndex = -1

for i in range(numarrays):
	AddToGTO = 0
	Added = 0
#	print( narray[i], ContainedIn, AddToGTO, Added)
	Total = 0
	for j in narray[i]:
		if ContainedIn > 1:
			AddToGTO = 1 
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
					
	if AddToGTO == 1 and Added == 0 : 
		GTO.append(narray[[i]])
		Added = 1
	elif AddToGTO == 1 and Added == 1:
		break
	else:
		NGTO.append(narray[[i]])


print (*GTO, sep =",")
print ( *NGTO, sep =", ")
print(narray[CurIndex])
