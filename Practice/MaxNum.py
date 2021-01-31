# This is based on CareerCup Google tech question https://www.careercup.com/question?id=5699618401157120
# Given an array/list of numbers, using any combination of +-* operators
# Print the max possible number that can be generated using the numbers
# Example, Given list numbers 1,3,4,5 what is the max number - (1+3)*4*5  = 80
#
# In this example I learned at the expense of time that copyofarraya = arraya is not the same as copyofarraya = arraya.copy()
# I have not yet coded for negative numbers

#inputvalues = [3,5,0,1]
inputvalues = [0,5,1,0,1,1] # The array of numbers we want to maximise
sortedinputvalues = inputvalues.copy() # A copy of the values we want to maximise

#print (sortedinputvalues)

leninputvalues = len(inputvalues)
numones = 0
answer = 1

# How many 1s have I?
inputvalue = 0

for inputvalue in range (leninputvalues): # Loop through the input list/array
	# print (inputvalue, inputvalues[inputvalue])
	if inputvalues[inputvalue] == 1: # Keep track of the number of 1s we find
		numones +=1
		sortedinputvalues.remove(1) # Remove the 1s from the copied list
	if inputvalues[inputvalue] == 0: # Remove zeros from the copied list - we dont want to accidentally multiply by zero
		sortedinputvalues.remove(0)

sortedinputvalues = sorted(sortedinputvalues) # Sort the modified copied list so the smallest number is first
#print (sortedinputvalues)
#print(numones)

if numones == 1:
	sortedinputvalues[0] = sortedinputvalues[0] + 1 # If we only have 1 1 then add it to the smallest number in the list
for inputvalue in sortedinputvalues:
	answer = answer * inputvalue # Loop through our sorted list setting answer to answer times input value
if numones > 1:
	answer = answer * numones # If the number of 1s in the original list was greater than 1 then multiply the answer by the number of ones you had 
	
# Print your answer
print ("Max output from " + str(inputvalues) + " is :" + str(answer))
		

