#--------------ESTRUCTURA DE UNA API EN PYTHON-------------------
#1.- Necesitamos de una librería para extraer información de sitios wen "requests"
import requests
#2.- Necesitamos de una URL de donde vamos a extraer la información 
#3.- Con el método requests.get() pasamos el url 
#4.-Visualizamos el código de estado para confirmar la conexión al servidor

personaje = input(f"Personaje deseado\nOpciones:\nGoku-1\nVegeta-2\nPiccolo-3\n:")
if personaje == '1' or personaje == '2' or personaje=='3':

    url_personaje =f'https://dragonball-api.com/api/characters/{personaje}'
    r = requests.get(url_personaje)
    if r.status_code==200:
        print("Seguimos navegando exitósamente")
        data = r.json()

        name = data['name']
        descripcion = data['description']
        raza = data['race']
        ki = data['ki']
        print(f"--------------Nombre del personaje-------------: {name}") #Imprimimos nombre del personaje
        print("")
        print(f"-----------------Descripción de {name}-----------: {descripcion}") #Imprimimos la descripción del personaje
        print(f"\n-------------------Ki-----------------------: {data['ki']}")
        print(f"\n-------------------Raza:--------------------------:{raza}")
        while True:
            decision = input(f"Quieres guardar la información de {name}??: ").lower()
            if decision == 'si':
                print(f"GUardando datos de {name}")
                with open(f'Datos oficiales de {name}.txt','w') as file:
                    file.write(f'--------Datos Oficiales de {name}------------\n{descripcion}\nRaza:{raza}\nKi:{ki}')
                    break
            elif decision =='no':
                print("Muchas gracias por informar")
                break
            else:
                print(f"Respuesta no válida")
                continue
else:
    print("Personaje NO VÁLIDO")

