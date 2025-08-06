#Vamos a  realizar ejercicios que incluyan try, except, else, finally
import os
#try: lo que va a intentar
#except: Excepción o error
#else: si el try funciona
#finally: se ejecuta funcione el try o no

def dividir_10():
    try: #Pedimos el número al usuario por input
        print("Bienvenido, debes de ingresar un número que divida al cero")
        num = int(input("Número: "))
        resultado = 10/num
    except ZeroDivisionError: #Excepción de dividir entre o
        print("Error, no se puede dividir entre 0")
    except ValueError:
        print("ERROR, debe ser un dato numérico") #Excepción de valor
    else:
        print(f"El resultado es: {resultado}")
    finally:
        print("PROCESO TERMINADO, GRACIAS") #Mostrar esto siempre
    
#Expepcion con raise
def numero_positivo():
    try:
        numero = int(input("Ingresa un número POSITIVO: "))
        if numero <0: #Si el número es negativo
            raise ValueError("El número no debe de ser negativo") #Interrumpe el programa y va directamente al except
        print(f"Número correcto, mostraste: {numero}")
    except ValueError as e: #Guarda el mensaje del error en la variable "e"
        print(f"Mal {e}")
    finally:
        print("PROCESO TERMINADO")

#Expeción con manejo de archivos
def elegir_archivo():
    try:
        ruta = os.getcwd()
        print(f"Tu ruta es: {ruta} ")
        archivos = [f for f in os.listdir(ruta) if os.path.isfile(f)]
        print("Archivos disponibles:")
        for archivo in archivos:
            print(" -", archivo)
        arch = input("Ingresa tu archivo: ")
        with open(arch,'r',encoding='utf-8') as file:
            print(f"Contenido del archivo:\n{file.read()}") #Imprimimos el contenido de archivo
    except FileNotFoundError:
        print("NO SE PUDO ENCONTRAR EL ARCHIVO") #Mensaje de que el archivo no fue encontrado
    finally:
        print("PROCESO DE LEER ARCHIVO TERMINADO") #Siempre se ejecuta
elegir_archivo()
