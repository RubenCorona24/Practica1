#Probando los bucles y ciclos de python

#for : sirve para ir concatenando elementos de una lista, tupla, etc
#sintaxis: for i in [tupla.lista]

#while : sirve para hacer determinada acción mientras se cumpla algo
#sintaxis: while True:

lista = {'Federico','Rubén','Armando','Nicolás'}
for name in lista:
    print(f"Este usuario se llama {name}") #Imprimimos cada nombre de la lista

def probando_while(): #Función con bucle whiñe
    comenzar = True #variable booleano
    while comenzar: #empezamos con el bucle
        print("Bienvenido al bucle de python")
        detener = input("Quisieras detener este bucle?(si/no): ")
        if detener == 'no':
            print("Vale, vas a seguir en este bucle")
        elif detener == 'si':
            print("Muchas gracias por terminar con el bucle")
            comenzar = False #Se detiene el bucle 
        else:
            print("No diste una respuesta en concreto")

probando_while()

def funcion_par_impar(): #Función con if/else y for
    numero = int(input("escribe un número aleatorio: "))
    if numero%2 == 0:
        print("el número no es impar")
    else:
        print("El número es impar")
    

def probar_if_else(): #Función con if/else
    lista_preferencias = [] #lista vacia
    name = input("Introduce tu nombre: ")
    if name.isnumeric():
        print("Eso no es un nombre")
    else:
        lista_preferencias.append(name)
    deporte = input("Cuál es tu deporte favorito?: ")
    if deporte.isnumeric():
        print("Eso no es un deporte")
    else:
        lista_preferencias.append(deporte)
    comida = input("Alimento favorito: ")
    if comida.isnumeric():
        print("Eso no es una comida")
    else:
        lista_preferencias.append(comida)
    if len(lista_preferencias) == 3:
        print(f"Tu nombre es {name}, tu deporte favorito es: {deporte} y tu alimento favorito es: {comida}")
        print("Cumpliste con todos los formatos, bien")
    else:
        print("Parece que te faltan datos por resolver")
    return lista_preferencias

probar_if_else()

def probar_for(): #Función utilizando for
    numeros = range(1,11) #Los números en rango del 1 al 10
    for n in numeros:
        if n%2 == 0:
            print(f"{n} es un número par")
        else:
            print(f"{n} es un número impar")
    #La función nos devuelve por cada número si es par o impar

probar_for()    
    
    










    