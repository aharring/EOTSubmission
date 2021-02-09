# This is based on CareerCup Google tech question https://www.careercup.com/question?id=5699618401157120
# Given an array/list of numbers, using any combination of +-* operators
# Print the max possible number that can be generated using the numbers
# Example, Given list numbers 1,3,4,5 what is the max number - (1+3)*4*5  = 80
#
# In this example I learned at the expense of time that copyofarraya = arraya is not the same as copyofarraya = arraya.copy()
# * Looking at Negatives
# 	Two '-' make a plus so we only have to worry about '-' if we have an odd number of them, when we have an even number we multiply
#	We're going to need to track how many negatives we have

#inputvalues = [3,5,0,1]
inputvalues = [0,5,1,0,-9,-8,-3, 4] # The array of numbers we want to maximise

# So I think the biggest number you can get is
# discard the zeros, if there's more than 1 1 add them and use the total as a multiplier
# otherwise add 1 to the largest number and multiply
# if there's an even set of negatives multiply them out
# an odd negative should be subtracted at the end from the highest multiplied number

sortedinputvalues = inputvalues.copy() # A copy of the values we want to maximise
negatives = []

#print (sortedinputvalues)

leninputvalues = len(inputvalues)
numones = 0
numnegs = 0
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
	if inputvalues[inputvalue] < 0: # Track our negative values separately for now
                negatives.append(inputvalues[inputvalue])
                sortedinputvalues.remove(inputvalues[inputvalue])
                numnegs +=1

sortedinputvalues = sorted(sortedinputvalues) # Sort the modified copied list so the smallest number is first

#print (sortedinputvalues)
#print ( negatives)
#print(numones)

if numones == 1:
	sortedinputvalues[0] = sortedinputvalues[0] + 1 # If we only have 1 1 then add it to the smallest number in the list

for inputvalue in sortedinputvalues:
        answer = answer * inputvalue # Loop through our sorted list setting answer to answer times input value
if numones > 1:
	answer = answer * numones # If the number of 1s in the original list was greater than 1 then multiply the answer by the number of ones you had 
print (answer)

# If we have an odd number of negatives we want to remove the one that is closest to zero then multiply the others by our existing answer
# the one negative must be subtracted from the final answer
	
if numnegs > 1: 
        biggestneg = negatives[numnegs - 1]
        negatives.pop((numnegs-1))
        print ( biggestneg, negatives)
        for inputvalue in negatives :
            print (answer, inputvalue)
            answer = answer * inputvalue
elif numnegs == 1 :
        biggestneg = negatives[0]

print (sortedinputvalues)
print (biggestneg)
answer = answer + biggestneg

# Print your answer
print ("Max output from " + str(inputvalues) + " is :" + str(answer))
		

