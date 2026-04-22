#Listas : Se forman con corchetes []
nombres = ['Juan','Raul','Omar','Carlos']
nombres.append("Santiago") #Agregar al final

#Tuplas: Se forman con paréntesis () - Son INMUTABLES
coordenadas = (40.899,89.334)

#Diccionarios: Se forman con llaves {} para CLAVE-VALOR
usuario={
    'nombre': ['Jose','Angel','Yair'],
    'edad': [16,14,13]
}
print(f"Usuario: {usuario}")
print(f"Nombre usuario: {usuario['nombre']}")

#SET: Para elementos únicos  y operaciones matemáticas
languages_backend = {'Python','Java','Go'}
languages_frontend = {'JavaScript','Typescript','Python'}
full_stack = languages_backend & languages_frontend #{'Python'}

#-------------COMPRENSIONES-------------------: para tener el doble de eficiencia y más rápido
nun_pares = []
for n in range(1,3):
    if n%2==0:
        nun_pares.append(n**2) #Esto se puede reducir a una línea de código

num_pares =  [i**2 for i in range(10) if i%2==0 ] #Versión mejorada y más eficiente

#--------------MANEJO DE ERRORES----------------
def procesar_datos(archivo):
    try:
        with open(archivo,'r') as file:
            datos = file.read()
            return datos
    except FileExistsError:
        print("NO EXISTE EL ARCHIVO")
    except FileNotFoundError:
        print("NO SE ENCONTRÓ EL ARCHIVO")
    except Exception as e:  
        print(f"Error inesperado {e}") #Cualquier otro error