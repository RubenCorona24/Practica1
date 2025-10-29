positivos = negativos = ceros = 0
contador = 0
while contador<5:
    num = int(input("Introduce un número: "))
    if num>0:
        positivos +=1
    elif num<0:
        negativos+=1
    else:
        ceros +=1
    contador +=1
print(f"Positivos:{positivos}")
print(f"Negativos:{negativos}")
print(f"Ceros:{ceros}")

