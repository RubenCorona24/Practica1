#Vamos a rediseñar el código de asistencia de una manera gráfica con tkinter
import tkinter as tk
import face_recognition as fr
import cv2
import numpy as np
from PIL import Image,ImageTk
import os

#-----------CARGAR IMÁGENES DE EMPLEADOS------------
ruta = os.getcwd()
imagenes = []
empleados = []

for archivo in os.listdir(ruta):
    img = cv2.imread(f"{ruta}/{archivo}")
    if img is not None:
        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        codificado = fr.face_encodings(img_rgb)[0]
        imagenes.append(codificado)
        empleados.append(os.path.splitext(archivo)[0])

#----------FUNCIÓN PARA CAPTURAR Y RECONOCER------------
def capturar():
    global lbl_img
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    ret,frame = cam.read()
    cam.release()

    if not ret:
        lbl_resultado.config(text='Error al capturar la imagen',fg='red')
        return
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    caras = fr.face_locations(rgb_frame)
    codigos = fr.face_encodings(rgb_frame,caras)
    if not codigos:
        lbl_resultado.config(text="No se detectó ningún rostro", fg="orange")
        lbl_correcto.config(text='')
    else:
        for codif,cara in zip(codigos,caras):
            distancias = fr.face_distance(imagenes,codif)
            indice = np.argmin(distancias)

            if distancias[indice] <0.6:
                nombre = empleados[indice]
                lbl_resultado.config(text=f"Empleado: {nombre}",fg='green')
                t, r, b, l = cara
                cv2.rectangle(rgb_frame, (l, t), (r, b), (0, 255, 0), 2)
                cv2.putText(rgb_frame, nombre, (l, t - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                lbl_correcto.config(text='BIENVENIDO AL TRABAJO',foreground='blue',font=('Arial',16,'bold'))
            else:
                lbl_resultado.config(text="Empleado no reconocido", fg="red")
                lbl_correcto.config(text='')


    #convertir imagen a formato tkinter
    img_tk = ImageTk.PhotoImage(Image.fromarray(rgb_frame))
    lbl_img.config(image=img_tk)
    lbl_img.image = img_tk

#-----------INTERFAZ GRÁFICA-------------
ventana = tk.Tk()
ventana.title("Asistencia Facial")
ventana.geometry('600x900')
lbl_resultado = tk.Label(ventana,text="Presiona Capturar para iniciar",font=("Arial",14,'bold'))
lbl_resultado.pack(pady=10)
tk.Button(ventana,text='Capturar',command=capturar,foreground='red',font=("Arial",12,'bold')).pack(pady=10)
lbl_img = tk.Label(ventana)
lbl_img.pack()
lbl_correcto = tk.Label(ventana)
lbl_correcto.pack()






ventana.mainloop()