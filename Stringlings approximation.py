import math 
n=int(input("Enter the value of n for stringlings approximation "))
a=0
b=0
for k in range (1,n+1):
    a=math.log(k)
    b=b+a 
c=n*(math.log(n))-n
d=(b-c)/b
print (b)
print (c)
print ("Therefore the proportional error is ",d) 
