# Exploring lists 
# This program prints a random fruit
#

import random

# Define our list
fruitList = ["Apple", "Orange", "Pear", "Plum"]

fruitIndex = random.randint(0, len(fruitList)-1)
print("Random fruit chosen using index method : {}" .format(fruitList[fruitIndex]))

print("Random fruit choice of the day using random choice function: {}" .format(random.choice(fruitList)))

