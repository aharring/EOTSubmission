# Week 08 Using numpy 
# Lab :
# 1 Create a program that generates random numbers within a given range
# 2 Modify the program so it's the same 10 random numbers each time 
# 3 Add 5k to each of the salaries - calling this a bonus ;)
# 4 Increase the salaries by 5% 

import numpy as np

minSalary = 20000
maxSalary = 80000
numSalaries = 10

np.random.seed(1) # 2 This apparently ensures we get the same 10 random numbers each time the program is run

salaries = np.random.randint(minSalary, maxSalary, numSalaries) # 1 Generate 10 random numbers 20000-80000
salariesPlusBonuses = salaries + 5000 # 3 Increase each salary by 5k. Adding is easier with numpy
newSalaries = salaries * 1.05 # 4 Result is a float
newSalaries = newSalaries.astype(int) # 4 type casting to int doesn't work you have to do it the numpy way



print (salaries)
print(salariesPlusBonuses)
print(newSalaries)
