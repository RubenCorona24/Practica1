# Agrupamiento por promedios K
Kmeans en python se utiliza para realizar agrupación (clustering) de datos no etiquetados, dividiendo el conjunto de datos en un número específico de grupos (k) basándose en la similitud entre los puntos de datos. Sirve para identificar patrones y estructuras naturales en los datos, minimizando la distancia entre cada punto y el centroide de su grupo. 
- Agrupar datos: Es la función principal. K-means agrupa puntos de datos en clústeres de forma no supervisada, lo que significa que no necesita etiquetas previas
- Identificar patrones: Permite descubrir relaciones y patrones ocultos en los datos.
- sintáxis: from sklearn.cluster import KMeans

# PCA (Análisis de Componentes Principales)
Se utiliza en Python para reducir la dimensionalidad de un conjunto de datos transformando un gran número de variables originales en un conjunto más pequeño de variables no correlacionadas (componentes principales), preservando la mayor cantidad de información y varianza posible.
- Reducción de dimensionalidad: Transforma datos de muchas dimensiones en un conjunto más manejable, lo que facilita el procesamiento y reduce la complejidad.
- sintáxis: from sklearn.descomposition import PCA

# SVD (Descomposición en valores singulares)
Sirve para descomponer una matriz en tres matrices más simples (\(U\), \(S\) y \(V^{T}\)), lo que se utiliza principalmente para la reducción de dimensionalidad, la compresión de imágenes, el filtrado de ruido y los sistemas de recomendación. Es una técnica de factorización matricial muy utilizada debido a su estabilidad. 
- Reducción de dimensionalidad: Al eliminar los valores singulares más pequeños, se pueden reducir las dimensiones de los datos conservando la mayor parte de su información importante, lo que es fundamental para el Análisis de Componentes Principales (PCA).
- sintáxis: U,sigma,Vt = np.linalg.svd(X)

