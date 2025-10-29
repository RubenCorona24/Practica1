#Traductor
def traductor():
    print("Menú de opciones de traductor:\n ")
    print("1.- Presiona 1 para convertir de español a inglés\n")
    print("2.- Presiona 2 para convertir de inglés a español")
    opcion = int(input("Escribe la opción que deseas usar(1,2): "))
    if opcion == 1:
        print("Conversor de español a inglés")
        opcion_uno = input("¿Cuál es la palabra que deseas traducir a inglés?: ")
        if opcion_uno == "hola":
            print("hellow")
        else:
            print("palabra desconocida")

    elif opcion == 2:
        print("Conversor de inglés a español")
        opcion_dos = input("¿Cuál es la palabra que deseas traducir a español?: ")
        if opcion_dos == "hellow":
            print("hola")
        else:
            print("La palabra se desconoce")
    #Tercer condicional
    else:
        print("Opción no disponible")


def ciclo():
    x = 1
    while x<7:
        print(x)
        x+=1
    print("Fin")
ciclo()

def ciclo_uno_dies():
    n = 1
    while n<11:
        print(n)
        n+=1
    print("Fin")
ciclo_uno_dies()