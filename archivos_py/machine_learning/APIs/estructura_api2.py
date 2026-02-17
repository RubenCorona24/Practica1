#--------------ESTRUCTURA DE UNA API EN PYTHON-------------------
#1.- Necesitamos de una librería para extraer información de sitios wen "requests"
import requests
#2.- Necesitamos de una URL de donde vamos a extraer la información 
url = 'https://dragonball-api.com/api/characters/1'
#3.- Con el método requests.get() pasamos el url 
r = requests.get(url)
#4.-Visualizamos el código de estado para confirmar la conexión al servidor
if r.status_code == 200:
    print(f"Seguimos navegando exitosamente")
    #Guardamos los datos json con el método r.json()
    data = r.json()
    print(f"----------Datos del sitio web----------\n{data}")

