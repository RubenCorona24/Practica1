lista = [1,2,4,6,8,10,12,14]
def calcular_cuadrado(num):
    return num**2
def calcular_lista(numeros):
    for n in numeros:
        print(f"El cuadrado de {n} es {calcular_cuadrado(n)}")

def solicitar_nombre():
    name = input("Dime tu nombre: ")
    return name
def saludar(name):
    print(f"¡Hola {name}!")

def pedir_numeros():
    num1= int(input("First numer: "))
    num2= int(input("Second numer: "))
    return num1,num2
def sumar():
    n1,n2 = pedir_numeros()
    suma = n1+n2
    print(f"La suma es {suma}")

def solicitar_numero():
    num = int(input("Ingrese un número entero positivo: "))
    return num
def calcular_factorial(num):
    r=1
    for n in range(1,num):
        r*=n
    return r
def mostrar_resultado():
    num = solicitar_numero()
    re = calcular_factorial(num)
    print(f"El factorial de {num} es {re}")
    
#Consigna
#crear una tabla de multiplicar donde se le pregunte al usuario el numero y el limite, al finalizar preguntar si quiere otra tabla o no
def tabla_multiplicar(num,limite):
    iteracion = 1
    for n in range(limite):
        print(f"{num}x{iteracion}: {num*iteracion}")
        iteracion +=1
def hacer_tabla():
    while True:
        numero = int(input("Cuál es el número que quieres multiplicar?: "))
        limite = int(input("Cuál es el límite de tu multiplicación?(hasta donde multiplicar): "))
        if numero and limite:
            print(f"Bien, hemos hecho una tabla del número {numero} que multiplica hasta {limite}\n")
            tabla_multiplicar(numero,limite)
        else:
            print("No has llenado todas las tablas")
        eleccion = input("Deseas realizar otra tabla? (si/no): ")
        if eleccion == 'si':
            continue
        elif eleccion =='no':
            print("Gracias!!")
            break
        else:
            print("No has dado una respuesta clara  ??")



