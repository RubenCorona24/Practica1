#crear un archivo y ahí mismoescribir
import os
ruta = os.getcwd()
print(f"Estamos en la ruta: {ruta}")
with open('saludo.txt','w') as archivo:
    archivo.write("Hola, bienvenido al curso de python")
#tarea completada

#leer el archivo anterior y mostrar su contenido
def mostrar_contenido():
    try:
        arch = input("Qué archivo deseas abrir?: ")
        with open(arch,'r') as file:
            print(f"Contenido del archivo:\n{file.read()}")
    except FileNotFoundError:
        print("Error, no se ha logrado encontrar el archivo")



#crear el archivo de tareas

archivo = open('tareas.txt','w')
arch_tareas = archivo.write("Esto es un archivo para guardar tus tareas\n")
archivo.close()

#crear lista de tareas
def lista_tareas():
    eleccion = input("Desea añadir una nueva tarea al archivo?(si/no): ")
    if eleccion == 'no':
        files = open('tareas.txt','r')
        notes = files.read()
        print(notes)
    elif eleccion == 'si':
        new_work = input("Seleccione su nueva tarea: ")
        files = open('tareas.txt','a')
        notes = files.write(new_work)
        print("Tarea agregada exitósamente")

lista_tareas()
lista_tareas()
lista_tareas()
