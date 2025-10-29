lista = [[56,34,1],[12,4,7],[9,3,4]]
for l in lista:
    print(l)

for l in lista:
    for i in l:
        print(i)
#Hacemos una iteración esta lista
print(lista[::-1])

#Iterar cadena al revés
def texto():
    texto = "python"
    for i in texto[::-1]:
        print(i)

#Iterar saltándose elementos
def bucle():
    texto2 = "Hola"
    for n in texto2[::2]:
        print(n)
def iterar():
    for i in range(0,5):
        print(i)
iterar()