import  matplotlib.pyplot as p
import numpy as np
x=np.random.uniform(-1,1,100000)
y=np.random.uniform(-1,1,100000)
xr=[]
yr=[]
for i in range (100000):
    if ((x[i]**2)+(y[i]**2))<=1:
        xr.append(i)
        yr.append(i)
        p.plot(xr,yr)
c=len(xr)
A=(4*c)/100000
print ("The area of a unit circle is ",A,"unit square")
