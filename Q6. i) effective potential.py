import numpy as np
import matplotlib.pyplot as pl
A=100
B=12
r=np.linspace(0.1,10,1000)
v=-(A/r)+(B/r**2)
pl.plot(r,v)
pl.xlabel('Value of r')
pl.ylabel('Ueff')
pl.grid(True)