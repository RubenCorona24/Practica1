#Vamos a realizar una comparación de rostros con reconocimiento facial
import cv2 #Procesa imágenes y videos
import numpy #Funciones de cv2 y fr trabajan con arrays de NumPy
import face_recognition as fr #Detecta, codifica y compara caras
#Primer paso: cargar imágenes
foto_control = fr.load_image_file('foto_santy.jpg') #Primera foto
foto_prueba  =fr.load_image_file('FotoA.jpg') #Segunda foto

#Pasar imágenes a rgb
foto_control = cv2.cvtColor(foto_control,cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba,cv2.COLOR_BGR2RGB)

#Localizar cara control
lugar_cara_santi = fr.face_locations(foto_control)[0]
cara_codificada_santi = fr.face_encodings(foto_control)[0]

lugar_cara_udemy = fr.face_locations(foto_prueba)[0]
cara_codificada_udemy = fr.face_encodings(foto_prueba)[0]

#mostrar_rectángulo
cv2.rectangle(foto_control,(lugar_cara_santi[3],lugar_cara_santi[0]),
              (lugar_cara_santi[1],lugar_cara_santi[2]),
              (0,255,0), #COLOR
              2) #BORDE
cv2.rectangle(foto_prueba,(lugar_cara_udemy[3],lugar_cara_udemy[0]),
              (lugar_cara_udemy[1],lugar_cara_udemy[2]),
              (0,255,0), #COLOR
              2) #BORDE

#Realizar comparación
resultado = fr.compare_faces([cara_codificada_santi],cara_codificada_udemy)


#medida de la distancia
distancia  =fr.face_distance([cara_codificada_santi],cara_codificada_udemy)
#mostrar resultado
# Mostrar texto sobre la imagen de prueba
texto = 'COINCIDE' if resultado[0] else 'NO COINCIDE'

# Puedes incluir la distancia como texto también si quieres
dist_texto = f'Distancia: {round(distancia[0], 2)}'

# Mostrar texto principal (Coincide o no)
cv2.putText(foto_prueba, texto, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
            1.2, (0, 255, 0) if resultado[0] else (0, 0, 255), 2)

# Mostrar la distancia debajo
cv2.putText(foto_prueba, dist_texto, (50, 90), cv2.FONT_HERSHEY_SIMPLEX,
            0.8, (255, 255, 255), 2)
#mostrar imágenes
cv2.imshow('Foto Santiago',foto_control)
cv2.imshow('Foto Udemy',foto_prueba)

#mantener el programa abierto
cv2.waitKey(0)

