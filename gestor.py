#imoportamos os para el manejo de archivos
import os
from pathlib import Path
carpeta = 'notas'
if not os.path.exists(carpeta):
    os.makedirs(carpeta)
#función de crear nota

def crear_nota():
    try:
        name = input("Nombre del archivo: ")
        nota = input("La nota de tu archivo:  ")
        file = open(name,'w')
        with open(f"{carpeta}/{name}.txt", "w", encoding="utf-8") as archivo:
            archivo.write(nota)
            print("Nota guardada exitosamente")

    except:
        print("Algo ha salido mal")


#función de de leer nota existente
def leer_nota():    
    name = input("Nombre de tu archivo existente: ")
    try:
        with open(f"{carpeta}/{name}.txt", "r", encoding="utf-8") as archivo:
            print("\n Contenido de la nota:")
            print(archivo.read())
    except FileNotFoundError:
        print("⚠️ Nota no encontrada.")


#función de listar todas las notas guardadas
def listar_notas():
    notas = os.listdir(carpeta)
    if notas:
        print("Notas guardadas exitosamente")
        for n in notas:
            print(f"- {n}")



#función de eliminar una nota
def eliminar_nota():
    nota = input("Nombre de tu archivo: ")
    ruta = Path(carpeta,nota.txt)
    if os.path.exists(ruta):
        os.remove(ruta)
        print("ruta eliminada exitosamente")
    else:
        print("FileNotFound")
    print("El archivo se ha eliminado")
#función de salir del programa
def menu():
    while True:
        print("\n--- MENÚ DEL GESTOR DE NOTAS ---")
        print("1. Crear una nota")
        print("2. Leer una nota")
        print("3. Listar notas")
        print("4. Eliminar una nota")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ")

        if opcion == '1':
            print("***Has escogido la opción de crear una nota***")
            crear_nota()
        elif opcion == '2':
            print("***Has escogido la opción de leer una nota***")
            leer_nota()
        elif opcion == '3':
            print("***Has escogido la opción de listar notas***")
            listar_notas()
        elif opcion == '4':
            print("***Has escogido la opción de eliminar una nota***")
            eliminar_nota()
        elif opcion == '5':
            print("***Has escogido la opción de salir***")
            print("Adiós, fue un gusyo apoyarte")
            break
        else:
            print("Opción no válida")

menu()

    
            
