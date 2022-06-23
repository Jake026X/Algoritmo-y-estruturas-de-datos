import pandas as pd
datos =        [["Luis",8,9,8,9],
                ["Jorge",5,4,6,5],
                ["Oscar",9,7,9,8],
                ["Adriana",7,5,7,6]]
columnas =['Alumno','Parcial 1','Parcial 2','Parcial 3','Promedio']
df = pd.DataFrame(datos,columns=columnas,)
porprom = df.sort_values('Promedio',ascending=False)
porprom.head()

print (df)
print (" ")
print (porprom)