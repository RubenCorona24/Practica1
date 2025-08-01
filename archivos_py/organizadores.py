#Función de obtener el nombre y calificación de alumnos
#from random import *
#def obtener_info(cantidad):
   # compañeros = []
   # for i in range(cantidad):
       # name = input("Introduce tu nombre: ")
       # notas = int(input(f"{name}, dime cuantas notas hiciste en el semestre (Max:5 Min:0): "))
       # asistencias = int(input("Asistencias en el semestre (Max:50): "))
       # def returnar_notas(notas):
          #  promedio = 0
           # if notas in range(0,3):
          #      promedio +=2
           # elif notas in range(3,5):
            #    promedio +=4
           # elif notas == 5:
          #      promedio+=6
         #   else:
        #        print("Inválido, máximas notas son 5")
       #     return promedio


       # def returnar_asistencias(asistencias):
      #      calif = 0
     #       if asistencias in range(0,20):
    #            calif +=1
   #         elif asistencias in range(20,50):
  #              calif += 3
 #           elif asistencias == 50:
#                calif +=4
#            else:
#                print("Error, no puedes tener esas asistencias")
#            return calif
#    califi_asistencias = returnar_asistencias(asistencias)
   #     calif_notass = returnar_notas(notas)
  #      promedio_general = calif_notass + califi_asistencias

 #       compañero = (name,promedio_general)
#        compañeros.append(compañero)
#    compañeros.sort(key=lambda x:x[1])
#    return compañeros

#print(obtener_info(3))


#Función para obtener el promedio mas alto y más bajo en alumnos

def obtener_alumnos(cantidad):
    compañeros = []
    for n in range(cantidad):
        name = input("Nombre del compañero: ")
        calificacion = float(input(f"Calificación de {name}: "))
        compañero = (name,calificacion)
        compañeros.append(compañero)

    compañeros.sort(key=lambda x:x[1],reverse=True)

    mejor = compañeros[0][0]
    peor = compañeros[-1][0]
    mejor_promedio = compañeros[0][1]
    peor_promedio = compañeros[-1][1]

    return mejor,peor,mejor_promedio,peor_promedio
try:
    asistencias = int(input("Cuántos compañeros asistieron a clase el día de hoy?: "))
    promedio_alto,promedio_bajo,mejor_promedio,peor_promedio = obtener_alumnos(asistencias)
    print(f"El promedio más alto es el de {promedio_alto}, con promedio de {mejor_promedio} \nY el promedio más bajo es el de {promedio_bajo}, con promedio de {peor_promedio} ")
except:
    print("Datos inválidos")
finally:
    print("PASE DE ASISTENCIA FINALIZADA")
        