#rutina para generar datos aleatorios 

from faker import Faker
import random

def crearListado():
    #crear una instancia de clase
    faker=Faker()

    #crear un listado de medicos
    medicos=[]

    #generar un ciclo de 1000 medicos
    for i in range(1000):
        #generar los nombres aleatorios
        nombre=faker.name()
        
        #geneara salarios
        salario=random.randint(2000000,10000000)

        #agrupar los datos
        medicos.append(
            {
                'id':i,
                'nombre':nombre,
                'salario':salario  
            }
        )
    return medicos