import tkinter as tk
import random

# Diccionarios de monstruos con pistas
mounstruos = {
    'vampiro': ['Le teme al sol','Tiene colmillos', 'Bebe sangre'],
    'zombi': ['Camina lento','Busca cerebros','Está medio podrido'],
    'bruja': ['Tiene escoba', 'Hace pociones', 'Usa sombrero pontiagudo'],
    'fantasma': ['Es blanco', 'Flota', 'Atraviesa paredes'],
    'esqueleto': ['No tiene carne','Hace ruido al caminar','Está en todos los cuerpos']
}

# Respuestas con emojis
respuestas = {
    'vampiro': "🧛",
    'zombi': "🧟",
    'bruja': "🧙‍♀️",
    'fantasma': "👻",
    'esqueleto': "💀"
}

# Selección aleatoria
monstruo = random.choice(list(mounstruos.keys()))
pistas = mounstruos[monstruo]

# Función para verificar respuesta
def verificar():
    respuesta = entrada.get().strip().lower()
    if respuesta == monstruo:
        resultado.config(text=f"✅ Correcto, era un {monstruo} {respuestas[monstruo]}", fg="green")
    else:
        resultado.config(text="❌ Incorrecto, sigue intentando", fg="red")

# Crear ventana
ventana = tk.Tk()
ventana.title("Adivina el Monstruo 👾")

# Mostrar pistas
tk.Label(ventana, text="Pistas:", font=("Arial", 14, "bold")).pack(pady=5)
for pista in pistas:
    tk.Label(ventana, text=f"- {pista}", font=("Arial", 12)).pack(anchor="w")

# Entrada de texto
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=10)

# Botón de verificación
boton = tk.Button(ventana, text="Comprobar", command=verificar, font=("Arial", 12))
boton.pack(pady=5)

# Resultado
resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
