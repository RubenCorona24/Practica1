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

#función de contador de palabras
def contador_palabras():
    carpeta = Path('notas')
    total_palabras = 0

    for arch in carpeta.glob("*.txt"):
        contenido = arch.read_text(encoding='utf-8')
        palabras = contenido.split()
        print(f"{arch.name}: {len(palabras)} palabras")
        total_palabras += len(palabras)

    print(f"En total el archivo: {arch.name} tiene {total_palabras} palabras")
    
#función de buscar palabra en una nota
def buscar_palabra():
    palabra= input("Escribe la palabra que deseas buscar: ").lower()
    carpeta = Path('notas')
    encontradas = []

    for arch in carpeta.glob('*.txt'):
        contenido = arch.read_text(encoding='utf-8').lower()
        if palabra in contenido:
            encontradas.append(arch.name)

    if encontradas:
        print("Palabras encontradas en estas notas: ")
        for name in encontradas:
            print(f"-{name}")
    else:
        print("No se encontró ningun archivo con esta palabra")

#función de salir del programa
def menu():
    while True:
        print("\n--- MENÚ DEL GESTOR DE NOTAS ---")
        print("1. Crear una nota")
        print("2. Leer una nota")
        print("3. Listar notas")
        print("4. Eliminar una nota")
        print("5. Contar palabras")
        print("6. Buscar palabra")
        print("7. Salir")
    
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
            print("***Has escogido la opción de contar palabras***")
            contador_palabras()
        elif opcion == '6':
            print("***Has elegido la opción de buscar palabra en notas")
            buscar_palabra()
        elif opcion == '7':
            print("***Has elegido la opción de salir***")
            print("Fue un gusto apoyarte, hasta pronto!!")
            break    

        else:
            print("Opción no válida")

menu()


    