def sumar(a,b):
    return a +b
def restar(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    if b!=0:
        return a /b
    else:
        print("Error, no se puede dividir entre 0")

opciones = {
    'sumar':sumar,
    'restar': restar,
    'multiplicar':multiplicar,
    'dividir':dividir
}

opcion = input("Decide la operación(sumar,restar,multiplicar,dividir): ")
valor_1 = int(input("Anota el primer valor: "))
valor_2 = int(input("Anota el segundo valor: "))
resultado = opciones[opcion](valor_1,valor_2)
print(f"El resultado de la {opcion} es {resultado}")

