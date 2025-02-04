# CALCULAR PRIMEDIO 
print("Bienvenidos a este sistema para calcular tu promedio de las materias")
nombre = str(input("¿cuál es tu nombre? "))
calif_esp = float(input("¿cual es tu calificacion de esp? "))
calif_mate = float(input("¿Cuál es tu calificación de matemáticas? "))
calif_historia = float(input("¿Cuál es tu calificación de historia? "))
promedio = (calif_esp + calif_mate + calif_historia) / 3
if promedio == 10:
    print("excelente")
elif promedio >= 9:
    print("Felicidades")
elif promedio >= 8:
    print("Bien")
else:
    print("reprobaste")
