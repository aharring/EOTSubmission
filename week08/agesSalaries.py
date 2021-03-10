# Week 08 
# Part 7
#      Two lists. 1 of salaries between 20k & 80K, the other and equivalent number of ages, so 50 salaries, 50 ages
#      Scatter plot
# Part 8
#      Add a line y=xsquared in a different colour
# Part 9
#      Add a legend, title and axis labels to this plot.
# Part 10
#      Save the picture
# Part 15 Add a line of normal distribution using Seaborn

import matplotlib.pyplot as mplt
import numpy as np
import seaborn as sns

minSalary = 20000
maxSalary = 80000
numEmployees = 100
minAge = 21
maxAge = 65

np.random.seed(1)

salaries = np.random.randint(minSalary, maxSalary, numEmployees)
np.random.seed(21) # Not exactly the same as the solution but just trying things out
ageEmployees = np.random.randint(minAge, maxAge, numEmployees)

#print (ageEmployees) # Just checking the ages are consistent every time 
xPoints = np.array(range(1,101))
yPoints = xPoints * xPoints

mplt.scatter(ageEmployees, salaries)
data = np.random.normal(46.0, 1.0, 100)
mplt.hist(data, 1)
#sns.kdeplot(data) # But what is the data. How do I make age & salary numbers plottable as a curve

mplt.plot(xPoints, yPoints, color = 'c', label ="x squared") # Cyan
mplt.title("GMIT Week 08 Python Labs - MatPlotLib") # Part 9 - making the graph look more presentable by adding a title, labels and a legend
mplt.xlabel("Employee Age")
mplt.ylabel("Employee Salary")
mplt.legend(loc = "upper right")

mplt.show()
mplt.savefig('prettier-plot.png')                    # 10 Save the picture. How cool is that.
