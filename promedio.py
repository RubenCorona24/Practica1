# CALCULAR PRIMEDIO 
print("Bienvenidos a este sistema para calcular tu promedio de las materias")
nombre = str(input("¿cuál es tu nombre?: "))
calif_esp = float(input("¿cual es tu calificacion de esp?: "))
calif_mate = float(input("¿Cuál es tu calificación de matemáticas?: "))
calif_historia = float(input("¿Cuál es tu calificación de historia?: "))
promedio = (calif_esp + calif_mate + calif_historia) / 3

def probar_promedio(promedio):


    if promedio == 10:
     print("Excelente, tuviste promedio perfecto")
    elif promedio >= 9:
            print("Felicidades, sigue así")
    elif promedio >= 8:
        print("Bien, pero necesitas mejorar más")
    else:
        print("Reprobaste, tienes que hacer extraordinarios")
try:
    probar_promedio(promedio)
except:
    print("incorrect data provided")
finally:
    print("Finished Process")








