#Definimos una función que suma los elementos de una lista
def sumar_lista(lista):
    suma =0
    for numero in lista:
        suma+=numero
    return suma
#Inicializamos la lista y el contador
numeros = []
contador = 0
#Pedimos a usuario cuántos números quiere ingresar
cantidad = int(input("¿Cuántos números quieres sumar?: "))
#Usamos while para recolectar los números
while contador <cantidad:
    entrada = int(input(f"Ingrese el número {contador +1}: "))
    numeros.append(entrada)
    contador+=1

#Usamos la función para calcular la suma
resultado = sumar_lista(numeros)
print(f"La suma total es: {resultado}")

