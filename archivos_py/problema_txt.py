#Dentro de un archivo txt, recopilar los nombres y apellidos de forma óptima
names= ['Camila','Rolando','Nicolás','Armando']
apellidos = ['´Gutierrez','Florencia','Espinoza','Jimenez']

with open('notas\\names_surnames.txt','w') as file: #Creamos el archivo en modo escritura con with
    file.writelines("Los datos son:\n\n")
    for n,a in zip(names,apellidos): #
        file.writelines(F"Nombre: {n}\napellido: {a}\n----------\n") #Escribimos la información en el archivo de textp

##zip() combina dos o más listas en pares---cada elemento de la primera fila se empareja con el elemento en la misma posición de la segunda lista.