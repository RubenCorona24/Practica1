


def suma_lista(lista):
    return sum(lista)
lista = [1,2,3,4,5]
resultado = (suma_lista(lista))
print(resultado)

def encontrar_maximo(lista):
    return max(lista)

numeros = [10,5,20,8]
print(f"El número más grande es: {encontrar_maximo(numeros)}")

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)
colores = ['rojo','verde','azul']
imprimir_lista(colores)

def agregar_elemento(lista,elemento):
    lista.append(elemento)
    return lista

frutas = ['manzana','plátano']
nueva_lista = agregar_elemento(frutas,'uva')
print(nueva_lista)

def suma_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

numeros = [4,7,2,9]
print(f"La suma de la lista es: {suma_lista(numeros)}")
#salida: La suma de la lista es: 22

def contar_ocurrencias(lista,elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador +=1
    return contador

frutas = ['manzana','pera','manzana','una','manzana']
print(f"La cantidad de 'manzana' es: {contar_ocurrencias(frutas,'manzana')}")
#salida: La cantidad de 'manzana es: 3


def filtrar_mayores(lista,limite):
    mayores = []
    for numero in lista:
        if numero > limite:
            mayores.append(numero)
    return mayores

numeros = [10,20,5,30,15,55,60]
print(filtrar_mayores(numeros,15))

def cuadrados(lista):
    cuadrados_lista = []
    for numero in lista:
        cuadrados_lista.append(numero*numero)
    return cuadrados_lista

numeros = [1,2,3,4,5]

print("Lista de cuasrados: ", cuadrados(numeros))

def encontrar_minimo(lista):
    return min(lista)
numeros = [10,5,20,8]
print(f"El número menor es: {encontrar_minimo(numeros)}")

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)
colores = ["rojo","verde","azul"]
imprimir_lista(colores)

saldo = 1000
def consultar_saldo():
    saldo = int(input("Cuál es tu saldo?: "))
    return saldo
def suma_lista(numeros):
    suma = 7
    for numero in numeros:
        suma += numero
    return suma
numeros = [4,7,2,9]
print(f"La suma de la lista es: {suma_lista(numeros)}")

def suma(a,b):
    return a + b
resultado = suma(5,3)
print(f"La suma es: {resultado}")

def multiplicar(a,b,c):
    return a*b*c
resultado = multiplicar(2,4,6)
print(f"El resultado de la multiplicación es: {resultado}")

def num_cuadrado(num):
    return num**3
resultado = num_cuadrado(9)
print(f"el resultado es {resultado}")

#función de ofrecer cosas
def ofrecer():
    cosas = ['vaso de agua','rebanada de pastel','copa de vino','rebanada de pizza']
    print(f"Ahorita lo que tenemos es: {cosas}")
    eleccion = input("Que deseas?: ")
    if 'vaso de agua' or 'agua' in eleccion:
        print("Por supuesto, ya mismo te doy un vaso de agua")
        fria_caliente = input("Lo quieres fría o tibia?: ")
        if 'fría'or 'fria' in fria_caliente:
            print("Dale, ya mismo un vaso de agua fria con hielos")
        elif 'tibia' in fria_caliente:
            print("Bien, entonces agua templada de la jarra")
        else:
            print("No entendí bien, pero te daré un vaso de agua tibia")
    elif 'rebanada de pastel' or 'pastel' in eleccion:
        print("Claro!!, ya mismo una tarta de pastel de chocolate si te apetece")
    elif 'copa de vino' or 'vino' in eleccion:
        vino = input("Si con gusto, el vino lo quieres tinto u oscura?: ")
        if 'tinto' in vino:
            print("Vale, ya mismo una copa de vino tinto para nuestro invitado")
        else:
            print("Vale, ya mismo una copa de vino oscura para nuestro invitado")
    elif 'rebanada de pizza' or 'pizza' in eleccion:
        pizza = input("Claro, tenemos de pepperoni o hawaiana: ")
        if 'pepperoni' or 'peperoni' in pizza:
            print("Dale, ahora te traigo una rebanada de pepperoni con gusto")
        else:
            print("Vale, ya mismo una rebanada de hawaiana con gusto")
    else:
        print("Lo sentimos, puedes ser más específico con tu pedido?")

def despedir():
    print("Adiós, que tengas buena suerte, y no olvides que aquí te recibimos a gusto.")


#funcion dentro de otra función (decoradores)

def devolver_saludo_despedida():
    elec = input("Do you want to go?: ")
    if elec == 'no' or 'not':
        print("Great!!, one moment please")
        ofrecer()
    elif elec == 'si' or 'yes':
        despedir()
    else:
        print("Lo siento, no pude entender tu mensaje")
try:
    devolver_saludo_despedida()
except:
    print("Sorry, what do you mean?")
finally:
    print("Finaliced process")





