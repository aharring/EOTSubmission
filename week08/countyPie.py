# Week 08 Lab
# Part 11
#      Have a list of counties from which you generate a list size 100 of possible counties from the smaller list
#      Draw a pie chart of representing the 100 choices
import numpy as np
import matplotlib.pyplot as mplt

possibleCounties = ['Dublin', 'Cork', 'Limerick', 'Clare', 'Kerry', 'Donegal', 'Galway'] # 7  counties

# Generate a random list of 100 counties for plotting using the 6 counties as the base choice, weight the distribution in p
counties = np.random.choice(possibleCounties, p=[0.14, 0.09, 0.05, 0.12, 0.28, 0.22, 0.1], size=(100))
colours = dict(zip(possibleCounties, mplt.cm.tab20.colors[:len(possibleCounties)])) # Setting up colours for the counties - from stack overflow
print(colours)

unique, counts = np.unique(counties, return_counts=True)
mplt.pie(counts, labels=unique, colors=[colours[key] for key in possibleCounties[1:]]) # Setting specific colours
mplt.title("GMIT Python Programming Wk8 - County Pie")
#mplt.bar(unique, counts)
mplt.show()
