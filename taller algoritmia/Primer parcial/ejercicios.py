def verificar_numero(n):
    if n >0:
        print("El número es positivo")
    elif n <0:
        print("El número es negativo")
    else:
        print("El número es cero")
#Solicitar numero al usuario
while True:
    numero = int(input("Ingresa el número: "))
    verificar_numero(numero)
    opcion = input("Deseas conocer otro número?: ")
    if opcion=='si':
        continue
    else:
        print("Hasta luego")
        break
