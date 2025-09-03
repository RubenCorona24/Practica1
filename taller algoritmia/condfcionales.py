print("Menú de opciones:\n ")
print("1.- Presiona 1 para convertir de número a palabra\n")
print("2.- Presiona 2 para convertir de palabra a número")
opcion = int(input("Escribe la opción que deseas usar(1,2): "))
if opcion == 1:
    print("Conversor de número a palabra")
    opcion_uno = int(input("¿Cuál es el número que deseas convtir a palabra?: "))
    if opcion_uno == 1:
        print("El número es UNO")
    else:
        print("El número se desconoce")

elif opcion == 2:
    print("Conversor de palabra a número")
    opcion_dos = input("¿Cuál es la palabra que deseas convertir a número?: ")
    if opcion_dos == "uno":
        print(F"El número es 1")
    else:
        print("El número se desconoce")
#Tercer condicional
else:
    print("Opción no disponible")
    