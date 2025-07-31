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
    while True:
        eleccion = input("Desea añadir una nueva tarea al archivo?(si/no/ver/salir): ").lower()
        if eleccion == 'no':
            print("No se guardó ninguna tarea")
        elif eleccion == 'si':
            new_work = input("Seleccione su nueva tarea: ")
            files = open('tareas.txt','a')
            notes = files.write(f"- {new_work}\n")
            print("Tarea agregada exitósamente")
        elif eleccion == 'salir':
            print("elegiste la opción de salir, hasta pronto!!!")
            break
        elif eleccion == 'ver':
            archivo = open('tareas.txt','r')
            readable = archivo.read()
            print(f"Contenido del archivo: {readable}")

        else:
            print("Lo siento, por ahora no has introducido una opción clara") 

lista_tareas()

