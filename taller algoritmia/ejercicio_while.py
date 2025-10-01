x = int(input("Escribe un npumero entero menor a 1000000: "))
while x <1000000:
    print(f"Este es tu número: {x}, y es menor que 230 entonces le voy a sumar +1 hasta llegar a 230")
    x+=1
if x==1000000:
    print("felicidades, llegamos al número")
else:
    print("No hubo necesidad de hacer la suma escribiste un npumero mayor")
print("Fin")