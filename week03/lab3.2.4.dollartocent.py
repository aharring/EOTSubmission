# Program requirements :
# 	Take input in dollars
# 	Convert it to cent
# 	Allow for negative numbers
#
#	Note : This program prints two results
#	In the first print out if you enter -5.996 or -5.994 it will print 599 cent
#	In the second print out if you enter -5.996 it will give 600 cent, if you enter -5.994 it will give 599 cent  

import math

dollarAmount = abs(float(input("Please enter the dollar amount to be converted : ")))

centAmount = int(dollarAmount * 100)
roundedCentAmount = int(round(dollarAmount * 100))

print("\n${} equates to {} cent  \n" .format(dollarAmount, centAmount))

print("\n${} equates to {} cent rounded  \n" .format(dollarAmount, roundedCentAmount))


