# Week 08
# Part 6 Write a program that plots a histogram of the salaries (from Question 1)
import matplotlib.pyplot as mplt
import numpy as np

minSalary = 20000
maxSalary = 80000
numSalaries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numSalaries)
#mplt.plot(salaries) # Simple join the dots graph
mplt.hist(salaries)  # Plot a histogram
mplt.show()
