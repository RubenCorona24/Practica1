
def inicio():
    print("Bienvenido al organizador de contenedores de basura")
    depositos = []
    while True:
        eleccion = input("¿de qué tipo es la basura? -1-Orgánica-  -2-No orgánica- -3:SALIR- -4:VER BASURA- : ")
        if eleccion == '1':
            print("Tu basura es orgánica")
            basura = input("Deposita tu basura: ")
            depositos.append(basura)
        elif eleccion == '2':
            print("Tu basura es inorgánica")
            basura = input("Deposita tu basura, objeto: ")
            depositos.append(basura)
        elif eleccion == '3':
            print("GRacias por tu elecciión, hasta luego!!")
            break
        elif eleccion =='4':
                if len(depositos) == 0:
                     print("Aún no hay depósitos")
                else:
                     
                    print("Vale, verás los depósitos que por ahora has dejado")
                    print(f"DEPÓSITOS: {depositos}")
        else:
            print("Opción inválida (1/2/3/4)")

inicio()
