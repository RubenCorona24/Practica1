#ALGORITMO DE APRENDIZAJE POR REFORZAMIENTO
#REDES Q PROFUNDAS (RQD)
#Importar librerías
import matplotlib.pyplot as plt
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential #Modelo utilizado
from keras.layers import Dense,Flatten
from keras.utils import to_categorical

#Cargar dataset mnist
(training_images,training_labels),(test_images,test_labels) = mnist.load_data() #60,000 to train, 10,000 to test

#Normalización de imagenes
training_images = training_images/255.0
test_images = test_images/255.0
#Normalización de etiquetas
training_labels = to_categorical(training_labels)
test_labels = to_categorical(test_labels)

#Definir la red neuronal
model = Sequential([Flatten(input_shape=(28,28)),
                    Dense(128,activation='relu'),
                    Dense(10,activation='softmax')])
#Flatten: convvierte la imagen de 28x28 en un vector de 784x1
#Dense: capa inicial de 128 neuronas-ReLU permite un aprendizaje rápido, capa final de 10 clases, softmax convierte salidas en posibilidades

#compilar el modelo
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy']) 
#adam: optimizador para redes neuronales profundas
#loss: mide que tanto se equivoca el modelo
#metrics accuracy: porcentaje de predicciones correctas


#Entrenar el modelo
model.fit(training_images,training_labels,epochs=5,validation_data=(test_images,test_labels))

#Generar predicciones del conjunto de datos
predicciones = model.predict(test_images)
def ver_imagen(array_predicciones,etiqueta_real,img):
    etiqueta_real,img = np.argmax(etiqueta_real),img.squeeze()
    plt.grid(False) #Desactivamos
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img,cmap=plt.cm.binary)
    #Mostrar etiqueta predicha
    etiqueta_predicha = np.argmax(array_predicciones)
    if etiqueta_predicha==etiqueta_real:
        color='green'
    else:
        color='red'
    #Establecemos el color del texto según los resultados
    plt.xlabel(f"Pred: {etiqueta_predicha} Real: {etiqueta_real}")

filas=5
columnas=3
num_imagenes = filas*columnas
plt.figure(figsize=(2*2*columnas,2*filas))
for i in range(num_imagenes): #Entramos en bucle según número de imágenes
    plt.subplot(filas,2*columnas,2*i+1)
    ver_imagen(predicciones[i],test_labels[i],test_images[i]) #Mostramos la imagen del número