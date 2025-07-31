import modulo_presentar as mp #Importamos otro módulo, con el fin de no volver a escribir las funciones

while True:  #Entramos en bucle
    try:
        nombre = input("Dime tu nombre completo: ")
        if nombre.isnumeric():
            print("Resultado mal dado")
            break
        pais = input("Introduce tu país: ")
        if pais.isnumeric():
            print("Resultado mal dado")
            break
        empresa = input('Introduce tu empresa de trabajo: ')
        if empresa.isnumeric():
            print("Resultado mal dado")
        print("Estamos accediendo a tus datos y formando tu curriculum")
        print(mp.presentar(nombre,pais,empresa))  #Imprime los datos
        
    except:
        print("Datos Inválidos")
    finally:
        print("Fin del proceso")
        break




