# Write a program (div.py) that reads in two numbers and
# divides the first one by the second and give the integer result and the
# remainder.

x = int(input("Please enter the numerator :"))
y = int(input("Please enter the denominator :"))
ans = x//y
remainder = x%y

print("{} divided by {} is {}. The remainder is {}" .format(x,y,ans,remainder))
