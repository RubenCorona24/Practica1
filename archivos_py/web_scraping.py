import csv
import requests
from bs4 import BeautifulSoup

#Función para obtener html
def obtener_html(url):
    # Configurar user agent con el fin de configurar bloqueos
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36' 
        }
        #Realizar la petición get
        respuesta = requests.get(url,headers=headers,timeout=10) #Va a esperar hasta 10 segundos
        if respuesta.status_code == 200: #Si no da ningún error
            return respuesta.text #Devuelve el texto de la respuesta (.text)
        else:
            print(f"Error al obtener la página: Código de estado {respuesta.status_code}")
            return None
    except Exception as e:
        print(f"Error al obtener la página {e}")
        return None


#Función de extraer títulos de noticias
def extraer_titulos(html): #De argumento recibe al html
    #crear el objeto BeautifulSoup para analizar el HTML
    soup= BeautifulSoup(html,'html.parser')
    #Buscar todos los elementos que podrían contener títulos de noticias
    titulos = []
    #Buscar elementos h1,h2,h3 
    for heading in soup.find_all(['h1','h2','h3']): #Pasamos por elmentos h1,h2,h3
        if heading.text.strip() and len(heading.text.strip()) >15: #verifica si el texto del heading.strip es mayor a 15caracteres, es un título
            titulos.append(heading.text.strip()) #Añade en la lista el texto del heading
            #Strip: elimina caracteres como los espacios en blanco
    #Buscar en elementos con clases comunes para títulos de noticias
    for elemento in soup.select('.title, .headline, .article-title, .news-title'):
        if elemento.text.strip() and elemento.text.strip() not in titulos:
            titulos.append(elemento.text.strip())
    return titulos


html = obtener_html('https://www.jornada.com.mx/') #Nos devuelve el html
print(extraer_titulos(html)) #Con la función extraer títulos, devuelve la lista de títulos



