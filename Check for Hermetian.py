
import numpy as np
d1=np.array([[0,1],[1,0]])
d2=np.array([[0,-1j],[1j,0]])
d3=np.array([[1,0],[0,-1]])
con1=np.conjugate(d1)
tran1=np.transpose(con1)
con2=np.conjugate(d2)
tran2=np.transpose(con2)
con3=np.conjugate(d3)
tran3=np.transpose(con3)
if d1.all()==tran1.all():
    print(d1)
    print(tran1)
    print("Sigma1 is a Hermitian matrix")
if d2.all()==tran2.all():
    print(d2)
    print(tran2)
    print("Sigma2 is a Hermitian matrix")
if d3.all()==tran3.all():
    print(d3)
    print(tran3)
    print("Sigma3 is a Hermitian matrix")
print("Thus all the Pauli spin matrices are Hermitian")