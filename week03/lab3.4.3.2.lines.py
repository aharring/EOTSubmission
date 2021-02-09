# To demonstrate unpacking
#
# Based on Lab week 3, section 4. Lists and tuples
# 
# Create a program called lines.py, in it: 
# Create an array that has tuples of x,y coordinates. 
# Print out the distance each of those points are from the origin.
#
import math

points = [(1,2),(3,3),(4,3)]
for x, y in points:
    dist = math.sqrt(x**2 + y**2)
    print ('point({},{}) is {:.2f} , from the origin'.format(x,y, dist))
