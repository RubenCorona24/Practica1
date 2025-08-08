#Vamos a programar una asistencia al trabajo por medio del reconocimiento facial
import cv2
import face_recognition as fr
import os
import numpy  #importamos librerias 
#cargar imágenes
ruta = 'archivos_aparte\\empleados' #Obtenemos la ruta
images = []
names_empleados = [] #creamos listas vacías de imagenes y nombres de empleados
lista_empleados = os.listdir(ruta)
for name in lista_empleados: #pasamos por cada empleado de la lista
        if name.endswith(('.jpg', '.jpeg', '.png')):
            ruta_imagen = os.path.join(ruta, name)
            imagen_actual = cv2.imread(ruta_imagen)

        if imagen_actual is None:
            print(f"❌ Error: no se pudo cargar la imagen '{name}'")
            continue  # Saltar esta imagen

        images.append(imagen_actual) #agregamos la imagen a la lista images
        names_empleados.append(os.path.splitext(name)[0]) #agregamos el nombre del empleado a la lista name_empleados

#Función codificar imágenes
def codificar(imagenes):
     lista_codificada = [] #creamos lista vacia de imágenes codificadas
     for imagen in imagenes:
          if imagen == None:
               continue
          imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
          codificaciones = fr.face_encodings(imagen)
          if codificaciones:
               lista_codificada.append(codificaciones[0])
          else:
               print("⚠️ No se detectó rostro en una imagen.")
     return lista_codificada

lista_empleados_codificada = codificar(images) #creamos lista de empleados codificada
captura = cv2.VideoCapture(0,cv2.CAP_DSHOW) #toma una captura de imagen
# captura
exito, imagen = captura.read() #Leer la captura, empaquetarlo en éxito,imagen

if not exito:
     print("ERROR, no se pudo tomar la captura")
else:
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB) #Pasar a rgb la imagen
    cara_captura = fr.face_locations(imagen)
    if not cara_captura:
         print("⚠️ No se detectó ningún rostro en la imagen.") #Mensaje no se detecto el rostro
    else:
         cara_captura_codificada = fr.face_encodings(imagen,cara_captura)
         for caracodif,caraubic in zip(cara_captura_codificada, cara_captura):
              coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
              distancias = fr.face_distance(lista_empleados_codificada, caracodif)
              indice_coincidencias = numpy.argmin(distancias)
              if distancias[indice_coincidencias] >0.6:
                   print("❌ No coincide con ninguno de nuestros empleados.")
              else:
                   nombre_empleado = names_empleados[indice_coincidencias]
                   print(f"✅ Bienvenido al trabajo {nombre_empleado}") #Mensaje de que se reconoció el rostro
                
captura.release()
cv2.destroyAllWindows() #Cerrar la cámara de captura