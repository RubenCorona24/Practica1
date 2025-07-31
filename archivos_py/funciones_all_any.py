#La función all() sirve para verificar que todos los elementos de una iterable sean True

#Requisitos
years = 18
calificacion = 8
asistencias  = 90


if all([years>=18],[calificacion>6],[asistencias>=80]):# True
    print("Cumples con todos los requisitos")  #Requiere aprobar todo

#Revisa que todos tengas más de tres letras
names = ['Griselda','Carlos','Roman']
if all(len(name)>2 for name in names):
    print("Todos los nombres tienen más de 3 letras") #Revisa que todos tengas más de tres letras

#Función any() Devuelve True si al menos uno es verdadero

print(any([66<12],[100==11],[10>9])) #True, 10>9
print(any('e' in nombre for nombre in names)) #True al menos un nombre contiene "e"