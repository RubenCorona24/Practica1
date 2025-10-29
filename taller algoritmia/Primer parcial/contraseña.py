import random
intentar = 0
pass_ok = "python2025"
while intentar<3:
    entrada = input("Ingresa la contraseña: ")
    if entrada == pass_ok:
        print("!Acceso concedido!")
        break
    else:
        print("Contraseña incorrecta")
        intentar +=1
if intentar ==3:
    print("Demasiados intentar: Acceso denegado")
    
#ctrl + shift + l (selecciona palabras con el msimo nombre)

