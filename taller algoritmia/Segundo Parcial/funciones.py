def contar_vocales(texto):
    vocales = 'aeiouAEIOU'
    return sum(1 for letra in texto if letra in vocales) #Encontramos si el texto tiene vocales

def es_palindromo(palabra):
    #Limpiamos la palabra: quitamos espacios y la convertimos en minúscula
    palabra = palabra.replace(" ","").lower()
    #Comparamos la palabra con su reverso
    return palabra == palabra[::-1]
#solicitar la entrada del usuario
while True:
    entrada = input("Ingresa una palabra o frase: ")
    if es_palindromo(entrada):
        print("!Es un palíndromo!")
        break
    else:
        print("No es un palindromo")
        continue

#Palindromo: Palabra que se lee de derecha a izquierda y viceversa de igual forma
