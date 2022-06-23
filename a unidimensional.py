import numpy as np
n = int(input("Ingrese el numero de Elementos: "))
xvec = np.zeros(n)
for i in range(n):
    t = str(i)
    x = float(input("Ingrese el valor de x"+ t + ": "))
    xvec[i]=(x)

print (xvec)