#10- Traductor
nombre = input("antes de comenzar escribe tu nombre ")
print( " **** selecciona una opción ****")
print(nombre + " presiona 1 para traductor de colores: inglés a español")
print(nombre + " presiona 2 para traductor de colores: español a inglés")
print(nombre + " presiona 3 para traductor de colores: español a francés")
print("*********")
opcion = int(input("Escribe la opción que deseas usar: "))
#opción 1 Inglés a Español
if opcion == 1:
    print("Elegiste inglés a español")
    opcion_uno = input("escribe la palabra que deseas traducir ")
    if opcion_uno == "blue":
         print("La palabra es AZUL")
    elif opcion_uno == "brown":
        print("la palabra es CAFE")
    elif opcion_uno == "red":
        print("la palabra es ROJO")
    elif opcion_uno == "orange":
        print("la palabra es NARANJA")
    elif opcion_uno == "yellow":
        print("La palabra es AMARILLO")
    elif opcion_uno == "black":
        print("la palabra es MORADO")
    else:
        print("no se conoce el color")


    #Opción 2 Español a Inglés
elif opcion == 2:
    print("traductor de español a inglés")
    opcion_dos = input("que palabra deseas traducir? ")
    if opcion_dos == "azul":
        print("the color is BLUE")
    elif opcion_dos == "morado":
        print("the color is PURPLE")
    elif opcion_dos == "rojo":
        print("the color is RED")
    elif opcion_dos == "naranja":
        print("the color is ORANGE")
    elif opcion_dos == "negro":
        print("the color is BLACK")
    else:
        print("the color is not known")

    #Opción 3 español a francés
elif opcion == 3:
    print("traductor de español a francés")
    opcion_tres = input("que palabra deseas traducir? ")
    if opcion_tres == "azul":
        print("le mot est bleu")
    elif opcion_tres == "morado":
        print("le mot est violet")
    elif opcion_tres == "rojo":
        print("le mot est rouge")
    elif opcion_tres == "naranja":
        print("le mot est orange")
    elif opcion_tres == "negro":
        print("le mot est noir")
    else:
        print("no se conoce el color")
          

    #Opcion no válida
else:
    print("Opción no válida")