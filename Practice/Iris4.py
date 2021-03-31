# Attempting to manipulate Iris data without using numpy, pandas etc - just straight manipulation of the data in order to practice list & dicts

import csv 

Iris = {
    "Setosa" : {
        "Traits" : {
            "Sepal Width" : [],
            "Sepal Length": [],
            "Petal Width" : [],
            "Petal Length": []
         }
    },

    "Virginica" : {
        "Traits" : {
            "Sepal Width" : [],
            "Sepal Length": [],
            "Petal Width" : [],
            "Petal Length": []
        }
    },

    "Versicolor" : {
        "Traits" : {
           "Sepal Width" : [],
           "Sepal Length": [],
           "Petal Width" : [],
           "Petal Length": []
        }
    },

    "All" : {
        "Traits" : {
           "Sepal Width" : [],
           "Sepal Length": [],
           "Petal Width" : [],
           "Petal Length": []
        }
    }

}

traits = ["Sepal Width", "Sepal Length", "Petal Width", "Petal Length"]               # So we can loop through traits in each variety

# Function to calculate the Median
def calcMedian(list):
    mid = len(list)//2
    if len(list) % 2: # Odd length List
            return list[mid]
    else:
        med = (list[mid] + list[mid-1]) / 2  # Even length List
        return med

# Function to calculate the mode(s)
def calcMode(list):
    # for each entry in the list, if it's not in D add it as a key and increment it's occurrence by 1
    # d will look like this .. as an example
    # {3.5 :6, 2.1 :1, 5:1, 2.2:3, 3.3:6}
    # x is the 3.5 part, y is the 6 part
    # if more than one item has the max occurrence then all items with the max will be returned
    # In the example both 3.5 and 3.3 would be returned because they both have 6

    d = {}
    for i in list:
        if not i in d:
            d[i]=1
        else:
            d[i]+=1
    #for x,y in d.items() :
    #    print(x, y)

    return [x for x,y in d.items() if y==max(d.values())] 

# Function to calculate Average per variety trait
def calcAvg(list):
    return sum(list)/len(list)  # Average

# The main program
# Open the csv file
# Get the float value of each trait
# Add these values to two lists
# List 1. Contains all the data for a given trait
# List 2. Contains the data for a trait for a given variety
# The lists are stored in a dictionary
#
with open('Iris.csv', newline='') as csvfile:
     irisData = csv.DictReader(csvfile)
     for iris in irisData:
         #print (iris)

         curSepalLength = float(iris["sepal.length"])
         curSepalWidth = float(iris["sepal.width"])
         curPetalWidth = float(iris["petal.width"])
         curPetalLength = float(iris["petal.length"])

         Iris["All"]["Traits"]["Sepal Width"].append(curSepalWidth)
         Iris["All"]["Traits"]["Sepal Length"].append(curSepalLength)
         Iris["All"]["Traits"]["Petal Width"].append(curPetalWidth)
         Iris["All"]["Traits"]["Petal Length"].append(curPetalLength)

         if iris["variety"] == 'Setosa' :

            Iris["Setosa"]["Traits"]["Sepal Width"].append(curSepalWidth)
            Iris["Setosa"]["Traits"]["Sepal Length"].append(curSepalLength)
            Iris["Setosa"]["Traits"]["Petal Width"].append(curPetalWidth)
            Iris["Setosa"]["Traits"]["Petal Length"].append(curPetalLength)

         elif iris["variety"] == 'Virginica' :
 
            Iris["Virginica"]["Traits"]["Sepal Width"].append(curSepalWidth)
            Iris["Virginica"]["Traits"]["Sepal Length"].append(curSepalLength)
            Iris["Virginica"]["Traits"]["Petal Width"].append(curPetalWidth)
            Iris["Virginica"]["Traits"]["Petal Length"].append(curPetalLength)

         elif iris["variety"] == 'Versicolor' :
 
            Iris["Versicolor"]["Traits"]["Sepal Width"].append(curSepalWidth)
            Iris["Versicolor"]["Traits"]["Sepal Length"].append(curSepalLength)
            Iris["Versicolor"]["Traits"]["Petal Width"].append(curPetalWidth)
            Iris["Versicolor"]["Traits"]["Petal Length"].append(curPetalLength)

# Process the data
#print(Iris)
for variety in Iris :                                         # Loop through the dict keys Setosa, Versicolor, Virginica and All. For each trait in list traits
    for trait in traits :
        Iris[variety]["Traits"][trait].sort()                 # Sort the trait list in to asc order. Needed for Median & Range calculations
        avg = calcAvg(Iris[variety]["Traits"][trait])         # Calculate the average per trait
        median = calcMedian(Iris[variety]["Traits"][trait])   # Calculate the median  per trait
        mode = calcMode(Iris[variety]["Traits"][trait])       # Calculate the mode(s) per trait
                                                              # Calculate standard deviation per trait - function not written yet

       # Print Range, Average,  Median, Mode per trait, per variety
        print("{} {}\n" .format(variety, trait))
        print("Average : {}\nMedian : {}\nMode : {}\nRange : {} - {}\n" .format(avg, median, mode, Iris[variety]["Traits"][trait][0], Iris[variety]["Traits"][trait][-1]))
       
