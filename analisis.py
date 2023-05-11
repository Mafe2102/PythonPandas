import pandas as pd

#obteniendo datos de una fuente

tabla=pd.read_csv("./data/empleados.csv")
print (tabla)
print("\n")
#print(tabla.head(50))
print("\n")
#print(tabla.tail(10))
print(tabla[['nombres','salario']])
#como hacer para que nos muestre todos


#traer una lista
from data.comidas import comidas
tabla2=pd.DataFrame(comidas,columns=['comida','valor'])
#print (tabla2)

from data.medicos import crearListado
medicos=crearListado()
tabla3=pd.DataFrame(medicos)
#print (tabla3)
