# Week 08 Lab
# Part 5 Plotting y = xsquared
import numpy as np
import matplotlib.pyplot as mplt

xPoints = np.array(range(1, 101))
yPoints = xPoints * xPoints

mplt.plot(xPoints, yPoints)
mplt.show()
