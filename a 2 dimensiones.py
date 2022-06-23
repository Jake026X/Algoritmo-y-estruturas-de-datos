import numpy as np
n = int(input("Ingrese el numero de Filas: "))
m = int(input("Ingrese el numero de columnas: "))
xvec = np.zeros((n,m))
for i in range(n):
    t = str(i)
    for k in range (m):
        q = str(k)
        x = float(input("Ingrese el valor de x"+ t + "," + q + ": "))
        xvec[i,k]=(x)

print (xvec)