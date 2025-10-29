numero_secreto = 7
intento = int(input("Adivina el número entre 1 y 10: "))
while intento!=numero_secreto:
    if intento<numero_secreto:
        print("Demasiado bajo")
    else:
        print("Demasiado alto")
    intento = int(input("Intenta de nuevo: "))
print(f"!Corecto!, El número era {numero_secreto}")
