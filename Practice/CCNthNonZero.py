# Print the nth occurrence of a non zero number in an array, 
arrayList = [0,9,0,0,0,0,6,12,0,18]
n = 3

for i in arrayList :

    if i !=0 :
        n -= 1
    if n == 0 :
       print ("The 3rd non zero element is {}" .format(i)) 
       break

x = [1,2,3,2,2,2,3,4]
list(filter((2).__ne__, x))
print(x)
