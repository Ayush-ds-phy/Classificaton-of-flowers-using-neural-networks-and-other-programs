
import numpy as np 
n=int(input("Enter the value of n"))
H=np.zeros((n,n),dtype=np.float64)
for i in range (n):
    for j in range (n):
        if(i==j):
            H[i,j]=0
        elif(abs(i-j)==1):
            H[i,j]=1
print()
print("----Hamiltonian Matrix----")
for row in H:
    print(*row)
    
print()
        
eigenvalues, eigenvectors =np.linalg.eig(H)
print("Eigenvalues: ",np.round(eigenvalues,2))
print("Eigenvectors: "),
print(np.round(eigenvectors,2))

print()

diag_h= np.diag(np.round(eigenvalues,2))
print("Diagonalized Matrix of H is :")
print(diag_h)
