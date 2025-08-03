#Importamos las librerias que vamos a necesitar

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio
import pyautogui
import requests
from random import *


#Función de transformar voz a texto
def trans_voz_a_texto():  ###FUNCIONA
    r = sr.Recognizer()  # Crear objeto reconocedor
    with sr.Microphone() as origen:  # Usar micrófono como fuente
        r.pause_threshold = 0.8  # Espera para considerar el final de la frase
        print("Ya puedes hablar")
        audio = r.listen(origen)  # Escuchar entrada de audio
        try:
            pedido = r.recognize_google(audio, language='es-MX')  # Reconocer voz
            print(f"Dijiste: {pedido}")
            return pedido
        except sr.UnknownValueError:
            print("No se ha detectado el audio.")
            return 'Sigo esperando'
        except sr.RequestError:
            print("No hay servicio.")
            return 'Sigo esperando'
        except Exception as e:
            print(f"No entendí el audio, lo siento: {e}")
            return 'Sigo esperando'

def hablar(mensaje): #Función para que el asistente hable  ###FUNCIONA
    engine = pyttsx3.init() #encender el motor de pyttsx3

    engine.say(mensaje)
    engine.runAndWait() #pronunciar el mensaje

def pedir_dia(): #Función para pedir el día de la semana  ###FUNCIONA
    dia = datetime.date.today() #crear variable con datos de hoy
    print(dia)
    today = dia.weekday() #crear variable para día de la semana
    print(today)
    calendario = {0:'Lunes',1:'Martes',2:'Miércoles',3:'Jueves',4:'Viernes',5:'Sábado',6:'Domingo'} #diccionario con nombres de días
    hablar(f"El día de hoy es {calendario[today]}") #decir el día de la semana

def decir_hora(): #Función para pedir la hora ###FUNCIONA
    hora = datetime.datetime.now() #crear variable con datos de la hora
    hora = f"En este momento son las: {hora.hour} horas con {hora.minute} minutos"
    hablar(hora)

def saludo_inicial(): #Función de saludo inicial al hablar  ###FUNCIONA
    hora = datetime.datetime.now()
    if hora.hour >= 20 or hora.hour < 6:
        momento ="Buenas noches"
    elif 6<=hora.hour<13:
        momento = 'Buenos día'
    else:
        momento = "Buenas tardes"


    hablar(f"Hola, {momento}, soy Valentina, tu asistente personal. Por favor dime en qué te puedo ayudar") #decir saludo##FRRF

def dato_curioso():
    datos = ['Los aguacates son una fruta, no una verdura. Técnicamente se consideran una baya de una sola semilla, lo creas o no.'
             ,'Una nube pesa alrededor de un millón de toneladas.',
             'Australia es más ancha que la Luna. La Luna tiene 3400 km de diámetro, mientras que el diámetro de Australia de este a oeste es de casi 4000 km.',
             'Los dientes humanos son la única parte del cuerpo que no puede curarse por sí misma. Los dientes están recubiertos de esmalte, que no es un tejido vivo',
             'Los antiguos romanos solían echar un trozo de pan tostado en el vino para tener buena salud, de ahí que brindemos.',
             'La gente es más creativa en la ducha. Cuando nos duchamos con agua caliente, experimentamos un mayor flujo de dopamina que nos hace más creativos.',
             'Las artes solían ser un deporte olímpico. Entre 1912 y 1948, los eventos deportivos internacionales otorgaban medallas a la música, la pintura, la escultura y la arquitectura.',
             'La Torre Eiffel puede ser 15 cm más alta durante el verano. Todo tiene una explicación: se debe a la expansión térmica que significa que el hierro se calienta, las partículas ganan energía cinética y ocupan más espacio.']
    dato_curioso = choice(datos)
    hablar(dato_curioso)


def centro_pedidos(): #Función de centro de pedidos
    saludo_inicial() #Activar el saludo inicial
    comenzar = True
    while comenzar:
        pedido = trans_voz_a_texto()
        if not pedido:
            continue
        pedido = pedido.lower()
        if 'dime la hora' in pedido or 'hora' in pedido:
            decir_hora()
            continue
        elif 'que día es hoy' in pedido or 'día' in pedido:
            pedir_dia()
            continue
        elif 'abre youtube' in pedido or 'abrir youtube' in pedido or 'youtube' in pedido:
            hablar("Con gusto, estoy abriendo youtube")
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abre github' in pedido or 'github' in pedido:
            hablar("Claro, ya estoy abriendo github")
            webbrowser.open("https://github.com/dashboard")
            continue
        elif 'abrir navegador' in pedido:
            hablar("Por supeusto, abriendo google")
            webbrowser.open('https://www.google.com')
            continue
        elif 'busca en Wikipedia' in pedido:
            hablar("Claro, buscando en Wikipedia")
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido,sentences=1)
            hablar(f"Wikipedia dice lo siguiente: ")
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar("Claro, buscando en internet")
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif 'adiós' in pedido:
            hablar("Claro, fue un gusto ayudarte")
            comenzar  =False
        elif 'reproducir' in pedido:
            hablar("Buena idea, ya mismo la reproduzco")
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido or 'chiste' in pedido:
            hablar("Por supuesto, hechale un vistazo a esta broma")
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL', 'amazon': 'AMZN', 'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yfinance.Ticker(accion_buscada)
                respuesta = accion_buscada.info['regularMarketPrice']
                hablar(f"La encontré, el precio de {accion} es {respuesta}")
                continue
            except:
                hablar('Ups, ha habido un error, y no la he logrado encontrar, puedo brindarte información de google, amazon y apple')
        elif 'toma captura de pantalla' in pedido or 'screenshot' in pedido:
            hablar('Listo, he tomado una captura de pantalla')
            name_file = f"captura {datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            pyautogui.screenshot(name_file)
            hablar(f'La captura se ha guardado como: {name_file}')
            continue
        elif 'dato curioso' in pedido:
            hablar("Claro, a continuación, un dato curioso que no sabías hasta hace poco")
            dato_curioso()
            continue


centro_pedidos()