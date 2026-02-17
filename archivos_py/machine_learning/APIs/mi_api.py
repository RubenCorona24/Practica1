#API con la librería requests y el método GET
import requests
if __name__ == '__main__':
    url = 'https://ww.google.com.mx/'
    response = requests.get(url)
    if response.status_code == 200:
        contenido = response.content
        #Generamos nuevo archivo que contenga info de la página web
        with open('archivos_aparte/google_html','wb') as file:
            file.write(contenido) #insertamos el contenido de google
            print(f"Archivo guardado exitósamente")
    else:
        print(f"ERROR {response.status_code}, lo sentimos")