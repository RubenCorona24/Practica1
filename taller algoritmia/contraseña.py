import random
intentos = 0
pass_ok = "python2025"
while intentos<3:
    entrada = input("Ingresa la contraseña: ")
    if entrada == pass_ok:
        print("!Acceso concedido!")
        break
    else:
        print("Contraseña incorrecta")
        intentos +=1
if intentos ==3:
    print("Demasiados intentos: Acceso denegado")
    