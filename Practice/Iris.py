import csv

# Variable counter initialisation for each Iris Variety

countSetosa = 0
setosaSL = [] #0.0
setosaSW = [] #0.0
setosaPW = [] #0.0
setosaPL = [] #0.0

countVersicolor = 0
VersicolorSL = [] #0.0
VersicolorSW = [] #0.0
VersicolorPW = [] #0.0
VersicolorPL = [] #0.0

countVirginica = 0
VirginicaSL = [] #0.0
VirginicaSW = [] #0.0
VirginicaPW = [] #0.0
VirginicaPL = [] #0.0

countVarieties = 0
totalSL = [] #0.0
totalSW = [] #0.0
totalPW = [] #0.0
totalPL = [] #0.0

curSepalLength = 0.0
curSepalWidth = 0.0
curPetallength = 0.0
curPetalWidth = 0.0

avgSetosaSL =  0.0
avgSetosaSW = 0.0
avgSetosaPW =  0.0
avgSetosaPL = 0.0

avgVersicolorSL =  0.0
avgVersicolorSW = 0.0
avgVersicolorPW =  0.0
avgVersicolorPL = 0.0

avgVirginicaSL =  0.0
avgVirginicaSW = 0.0
avgVirginicaPW =  0.0
avgVirginicaPL = 0.0

avgTotalSL =  0.0
avgTotalSW = 0.0
avgTotalPW =  0.0
avgTotalPL = 0.0

medianSetosaSL = 0.0
medianSetosaSW = 0.0
medianSetosaPW = 0.0
medianSetosaPL = 0.0

medianVersicolorSL = 0.0
medianVersicolorSW = 0.0
medianVersicolorPW = 0.0
medianVersicolorPL = 0.0

medianVirginicaSL = 0.0
medianVirginicaSW = 0.0
medianViginicaPW = 0.0
medianVirginicaPL = 0.0

# Function to calculate the Median
#def calcMedian(list):
#    lenList = len(list)
##    index = lenList // 2
#    # Odd number in the list 
#    if lenList % 2:
#        return (list[index])
#    # Even number of entry in the list 
#    else :
#        return sum(list[index - 1:index + 1] / 2)

with open('Iris.csv', newline='') as csvfile:
     irisData = csv.DictReader(csvfile)

     for iris in irisData:

         countVarieties += 1                             # Counter to track total Irises
         curSepalLength = float(iris["sepal.length"])
         curSepalWidth = float(iris["sepal.width"])
         curPetalWidth = float(iris["petal.width"])
         curPetalLength = float(iris["petal.length"])

         totalSL.append(curSepalLength)
         totalSW.append(curSepalWidth)
         totalPW.append(curPetalWidth)
         totalSL.append(curPetalLength)

         if iris["variety"] == 'Setosa' :
             countSetosa +=1
             setosaSL.append(curSepalLength)
             setosaSW.append(curSepalWidth)
             setosaPW.append(curPetalWidth)
             setosaPL.append(curPetalLength)
         elif iris["variety"] == 'Versicolor' :
             countVersicolor +=1
             VersicolorSL.append(curSepalLength)
             VersicolorSW.append(curSepalWidth)
             VersicolorPW.append(curPetalWidth)
             VersicolorPL.append(curPetallength)
         elif iris["variety"] == 'Virginica' :
             countVersicolor +=1
             VirginicaSL.append(curSepalLength)
             VirginicaSW.append(curSepalWidth)
             VirginicaPW.append(curPetalWidth)
             VirginicaPL.append(curPetalLength)


# Sort the data - 

setosaSL.sort()
setosaSW.sort()
setosaPW.sort()
setosaPL.sort()

VersicolorSL.sort()
VersicolorSW.sort()
VersicolorPW.sort()
VersicolorPL.sort()

VirginicaSL.sort()
VirginicaSW.sort()
VirginicaPW.sort()
VirginicaPL.sort()

# Calculate averages for each varitey

avgSetosaSL = sum(setosaSL)/len(setosaSL)
avgSetosaSW = sum(setosaSW)/len(setosaSW)
avgSetosaPW = sum(setosaPW)/len(setosaPW)
avgSetosaPL = sum(setosaPL)/len(setosaPL)

avgVersicolorSL = sum(VersicolorSL)/len(VersicolorSL)
avgVersicolorSW = sum(VersicolorSW)/len(VersicolorSW)
avgVersicolorPW = sum(VersicolorPW)/len(VersicolorPW)
avgVersicolorPL = sum(VersicolorPL)/len(VersicolorPL)

avgVirginicaSL = sum(VirginicaSL)/len(VirginicaSL)
avgVirginicaSW = sum(VirginicaSW)/len(VirginicaSW)
avgVirginicaPW = sum(VirginicaPW)/len(VirginicaPW)
avgVirginicaPL = sum(VirginicaPL)/len(VirginicaPL)

# Calculate the average across varieties

avgTotalSL = sum(totalSL)/countVarieties 
avgTotalSW = sum(totalSW)/countVarieties 
avgTotalPW = sum(totalPW)/countVarieties 
avgTotalPL = sum(totalPL)/countVarieties 

# Calculate the median across each variety/feature
#medianSetosaSL = calcMedian(setosaSL)
#medianSetosaSW = calcMedian(setosaSW)
#medianSetosaPW = calcMedian(setosaPW)
#medianSetosaPL = calcMedian(setosaPL)

#print ("\nThere are {} Setosa in the sample.\nThe sum of the sepal lengths in this variety is {}.\nThe sum of the petal widths in this variety is {} \nThe sum of petal lengths in this variety is {}\n" .format(countSetosa, setosaSL, setosaPW, setosaPL))

irisDataPtr = csv.reader(open('Iris.csv', 'r'), delimiter = ',')
irisData = list(zip(*irisDataPtr))
print(irisData)
