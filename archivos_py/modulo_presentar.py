def presentar(name,country,empleado):
    return f"Hola, mi nombre es {name}, soy de {country}, y soy empleado en {empleado} "

def acceder(código):
    while True:
        try:
            code = int(input("Código de acceso: "))
            if code == código:
                print("Está bien. tu código es correcto")
                break
            else:
                print("Tu código es incorrecto")
        except:
            print("Debes de ingresar números")
            