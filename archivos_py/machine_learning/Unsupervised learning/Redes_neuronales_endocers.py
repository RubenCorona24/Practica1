#REDES NEURONALES
#Importamos las librerías
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digitos = load_digits()
print(digitos['data'][0]) #Mostramos el índice 0 de datos del array
digits = digitos['data'][0].reshape(8,8) #Reorganizamos el array a una dimensionm 8,8 con reshape
plt.imshow(digits) #Mostramos la imagen con plt.imshow
plt.imshow(digitos.images[2]) #Forma más simple de visualizar
#Creamos la variable independiente (X) en este caso es: digitos.data
X = digitos.data
#Normalizamos los datos
X = X/16.0
#Dividimos en entrenamiento/prueba
X_train,X_test = train_test_split(X,train_size=0.8,random_state=42)
#Creamos una variable llamada imagen_entrada: contiene un Input con un shape de (64, )
imagen_entrada = Input(shape=(64, ))
#Creamos un codificado que contiene: Densidad de 32, activacion = 'relu', y recibe imagen_entrada
codificado = Dense(32,activation='relu') (imagen_entrada)
#Creamos un decodificado que contiene: Densidad de 64, activación='sigmoid', y recibe al codificado
decodificado = Dense(64,activation='sigmoid') (codificado)
#Creamos el encoder con Model()
autoencoder = Model(imagen_entrada,decodificado) #Pasamos de argumento a la imagen de entrada y al decodificado
#Compilamos el autoencoder con **.compile()** con optimizer='adam', loss='binary_crossentropy'
autoencoder.compile(optimizer='adam',loss='binary_crossentropy') #El modelo autoencoder está configurado y es momento de entrenarlo
#Entrenamos al modelo con .fit() pasando como argumento dos veces a X_train
autoencoder.fit(X_train,X_train,epochs=100,batch_size=256,shuffle=True,validation_data=(X_test,X_test))
#epochs=100: se repasa 100 veces todo el conjunto de entrenamiento
#bach_size: indica que el modelo toma 26 ejemplos de X_entrena, actualizar, procesa, pasar al siguiente lote de 256 ejemplos más
#shuffle=true: los datos se mezclan antes de cada epoch
#validation_data: usamos dos veces X_test
#Todo esto inicia el procesa el poroceso de entrenamiento del autoencoder y lo alimenta con datos de entrenamiento: cuantas veces repasar los datos(en qué orden) y comprobar el aprendizaje
#Entramos en un loop que se repite 10 veces, hacemos un ploteo con: 2x10, i + 1(posición de cada gráfico en el índice de subplots),  plt.imshow(X_test en el índice i) con un reshape de 8x8
# Visualizamos 10 imágenes originales y sus reconstrucciones

for i in range(10):
    # --- Imagen original ---
    # Creamos un subplot en una rejilla de 2 filas y 10 columnas.
    # La primera fila muestra las imágenes originales.
    plt.subplot(2, 10, i + 1)
    plt.imshow(X_test[i].reshape(8, 8), cmap="gray")
    plt.axis("off")  # Ocultamos ejes para que se vea más claro

    # --- Imagen reconstruida ---
    # Predicción del autoencoder: hay que darle una forma (1,64)
    reconstruida = autoencoder.predict(X_test[i].reshape(1, 64))[0]

    # Segunda fila, imágenes reconstruidas por la red
    plt.subplot(2, 10, i + 1 + 10)
    plt.imshow(reconstruida.reshape(8, 8), cmap="gray")
    plt.axis("off")

plt.suptitle("Original (fila 1) vs Reconstrucciones del Autoencoder (fila 2)")
plt.show()
