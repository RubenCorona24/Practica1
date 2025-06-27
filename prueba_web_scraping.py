#Importamos las librerias bs4 y requests
import bs4
import requests
#Aprenderemos a usar web scraping,
# en este caso sobre los libros que tengan tres o más estrellas de reseña

url  = 'https://books.toscrape.com/catalogue/page-{}.html'


#crear lista de libros de mejor calificacion
libros_rating_alto = []

#crear un loop para cada página de el sitio web
for pagina in range(1,51):

    #crear una pagina a cada numero
    url_pagina = url.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,'html.parser')

    #seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    #hacer una iteración de cada libro
    for libro in libros:
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) !=0:

            #guardar titulo en variables
            titulo_libro= libro.select('a')[1]['title']
            #agregar el libro a la losta
            libros_rating_alto.append(titulo_libro)
try:
#crear un iterador para mostrar libros
    for t in libros_rating_alto:
        print(t)
except:
    print("***Failed system***")

else:
    print("***Successful system***")

finally:
    print("***End of the process***")