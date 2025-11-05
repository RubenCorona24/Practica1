#Arreglos
mi_array = [3,6,9,10,13,15,16]
print(mi_array[4]) #Imprimimos el índice 4, la cual le corresponde al 13

array = [7,12,9,4,11]
minVal = array[0] #El valor que vamos a buscar
for i in array: #Iteramos en el arreglo
    if i < minVal: #Si i es menor que el valor mínimo
        minVal=i #El valor minimo es i
print(f"Lowest value: {minVal}")

