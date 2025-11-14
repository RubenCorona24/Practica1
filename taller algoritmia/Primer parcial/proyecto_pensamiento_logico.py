import tkinter as tk
from tkinter import messagebox

# Ventana principal
ventana = tk.Tk()
ventana.title("Asistencia TEC")
ventana.geometry("700x600")   # más ancho para acomodar entradas horizontales

# Variables
nombre_var = tk.StringVar()
semestre_var = tk.IntVar()
materias = ['Español','Matemáticas','Historia','Ciencias','Inglés','Tecnología']
calificaciones_vars = [tk.DoubleVar() for _ in materias]
horas_vars = [tk.IntVar() for _ in range(5)]

# --- Funciones ---
def calcular_resultados():
    nombre = nombre_var.get()
    semestre = semestre_var.get()
    calificaciones = [v.get() for v in calificaciones_vars]
    promedio = sum(calificaciones)/len(calificaciones)
    horas_libres = sum([v.get() for v in horas_vars])

    resultado_text = f"Hola {nombre}, semestre {semestre}\n"
    resultado_text += f"Promedio general: {promedio:.2f}\n"
    resultado_text += f"Horas libres a la semana: {horas_libres}\n"

    if promedio >= 90:
        resultado_text += "¡Excelente! Vas muy bien, solo repasa un poco antes de tus exámenes.\n"
    elif promedio >= 70:
        resultado_text += "Vas bien, pero podrías aprovechar más tus horas libres para mejorar.\n"
    else:
        resultado_text += "Necesitas estudiar más. Usa tus horas libres sabiamente.\n"

    if promedio < 80 and horas_libres > 5:
        resultado_text += "Tienes tiempo disponible, úsalo para reforzar las materias más bajas.\n"

    resultado_label.config(text=resultado_text)

def mostrar_materias_bajas():
    calificaciones = [v.get() for v in calificaciones_vars]
    materias_menores = [materias[i] for i in range(len(materias)) if calificaciones[i] < 70]
    if materias_menores:
        messagebox.showinfo("Materias bajas", f"Con calificación menor a 70:\n{', '.join(materias_menores)}")
    else:
        messagebox.showinfo("Materias bajas", "¡No tienes materias con calificación menor a 70!")

def recomendar_horas():
    calificaciones = [v.get() for v in calificaciones_vars]
    recomendacion = ""
    for i in range(len(materias)):
        if calificaciones[i] >= 90:
            recomendacion += f"{materias[i]}: 1 hora\n"
        elif calificaciones[i] >= 70:
            recomendacion += f"{materias[i]}: 2 horas\n"
        else:
            recomendacion += f"{materias[i]}: 3 horas\n"
    messagebox.showinfo("Recomendación de estudio", recomendacion)

# --- Interfaz ---
tk.Label(ventana, text="-------- BIENVENIDO A LA ASISTENCIA TEC --------", font=("Arial", 12, "bold")).pack(pady=10)

# Nombre y semestre en horizontal
frame_info = tk.Frame(ventana)
frame_info.pack(pady=10)
tk.Label(frame_info, text="Nombre:").grid(row=0, column=0, padx=5)
tk.Entry(frame_info, textvariable=nombre_var).grid(row=0, column=1, padx=5)
tk.Label(frame_info, text="Semestre:").grid(row=0, column=2, padx=5)
tk.Entry(frame_info, textvariable=semestre_var, width=5).grid(row=0, column=3, padx=5)

# Calificaciones en horizontal
tk.Label(ventana, text="Introduce tus calificaciones:", font=("Arial", 12, "bold")).pack(pady=10)
frame_calif = tk.Frame(ventana)
frame_calif.pack(pady=5)
for i, mat in enumerate(materias):
    tk.Label(frame_calif, text=f"{mat}:").grid(row=0, column=i*2, padx=5, pady=5)
    tk.Entry(frame_calif, textvariable=calificaciones_vars[i], width=5).grid(row=0, column=i*2+1, padx=5, pady=5)

# Horas libres en horizontal
tk.Label(ventana, text="Horas libres por día (5 días):", font=("Arial", 12, "bold")).pack(pady=10)
frame_horas = tk.Frame(ventana)
frame_horas.pack(pady=5)
for i in range(5):
    tk.Label(frame_horas, text=f"Día {i+1}:").grid(row=0, column=i*2, padx=5, pady=5)
    tk.Entry(frame_horas, textvariable=horas_vars[i], width=5).grid(row=0, column=i*2+1, padx=5, pady=5)

# Botón calcular
tk.Button(ventana, text="Calcular resultados", command=calcular_resultados, bg="lightblue").pack(pady=10)

# Resultado
resultado_label = tk.Label(ventana, text="", font=("Arial", 11), justify="left")
resultado_label.pack(pady=10)

# Menú de opciones
tk.Label(ventana, text="--- MENÚ PRINCIPAL ---", font=("Arial", 12, "bold")).pack(pady=10)
tk.Button(ventana, text="1. Mostrar materias con baja calificación", command=mostrar_materias_bajas).pack(pady=5)
tk.Button(ventana, text="2. Recomendar horas de estudio por materia", command=recomendar_horas).pack(pady=5)
tk.Button(ventana, text="3. Salir", command=ventana.quit).pack(pady=5)

ventana.mainloop()
