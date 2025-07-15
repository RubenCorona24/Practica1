#VAMOS A CREAR UN REGISTRO DE DATOS PERSONALES
from datetime import *
#FUNCIÓN DE REGISTTRAR LOS DATOS
def registrar_datos():
    while True:
        elección= input("BIENVENIDO AL REGISTRO DE DATOS, QUE DESEA HACER?\n" \
        "1.- AGREGAR UN GASTO, MONTO, CATEGORÍA, DESCRIPCIÓÓN\n" \
        "2.- VER TODOS LOS GASTOS\n" \
        "3.- VER TOTAL GASTADO\n" \
        "4.- SALIR\n" \
        "RESPUESTA: ")
        if elección == '1':
            print("***Ha escogido la opción de agregar un gasto con su descripción***")
            try:
                monto = int(input("Cuanto es el monto gastado?: "))
            except ValueError:
                print("Debes de ingresar un número válido")
                continue
            uso = input("De que categoría es?(comida/transporte,etc): ")
            descripcion = input("Agrege una descripción de su monto: ")
            fecha = date.today()
            archivo = open('gastos.txt','a')
            rellenado = archivo.write(f"{monto}/{uso}/{descripcion}/{fecha}")
            print("Datos rellenados correctamente\n")
        elif elección == '2':
            print("***Ha escogido la opción de ver todos los gastos***")
            archivo = open('gastos.txt','r')
            readable = archivo.read()
            print(f"Gastos totales:\n{readable}")
        elif elección == '3':
            print("***Ha escogido la opción de ver el total de gastos***")
            total = 0
            archivo = open('gastos.txt','r')
            readable = archivo.read()
            for linea in readable:
                partes = linea.strip().split('/')
                if len(partes) >= 2:
                    try:
                        monto = float(partes[0].strip())  
                        total += monto
                    except ValueError:
                        pass
            print(F"\n💵Total gastado: {total:.2f}\n")
        elif elección == '4':
            print("***Ha escogido la opción de salir, hasta pronto!!***")
            break
        else:
            print("Opción no válida, vuelve a escoger (!/2/3/4): ")
registrar_datos()