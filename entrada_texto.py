mi_texto = open("Funciones.py")
una_linea = mi_texto.readline()
print(una_linea)

una_linea = mi_texto.readline()
print(una_linea)


una_linea = mi_texto.readline()
print(una_linea)


una_linea = mi_texto.readline()
print(una_linea)

otro_texto= open("for.py")

linea = otro_texto.readline()

def verificar_letra(texto):
    contador = 0
    for n in texto:
        if n == 'a':
            contador+=1
    return contador

texto = 'hola yo soy mateo'
def mover_o(texto):
    if 'o' in texto:
        texto.replace('o','a')

print(mover_o(texto))

print(verificar_letra(linea))


mi_texto.close()