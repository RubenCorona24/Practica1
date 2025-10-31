#Importamos la librería random
import random
#Diccionarios de mounstruos con pistas
mounstruos={
    'vampiro': ['Le teme al sol','Tiene colmillos', 'Bebe sangre'],
    'zombi': ['Camina lento','Busca cerebros','Esta medio podrido'],
    'bruja': ['Tiene escoba', 'Hace pociones', 'Usa sombrero pontiagudo'],
    'fantasma': ['Es blanco', 'Flota', 'Atraviesa paredes'],
    'esqueleto': ['No tiene carne','Hace ruido al caminar','Está en todos los cuerpos']
}
#Respuestas
respuestas = {
    'vampiro': "🧛",
    'zombi': "🧟",
    'bruja': "🧙‍♀️",
    'fantasma': "👻",
    'esqueleto': "💀"
}
#Selección aleatoria
monstruo = random.choice(list(mounstruos.keys()))
pistas = mounstruos[monstruo]
#.strip(): va a quitar los espacios en blanco (lo que no es )
#Mostrar pistas
for i,pista in enumerate(pistas,1):
    print(pista)
#Intento del usuario
respuesta = input("\n¿Quién crees que es?: ").strip().lower()
#Resultado
if respuesta==monstruo:
    print(f"Correcto!, era un {monstruo}")
else:
    print("Incorrecto, sigue intentando")