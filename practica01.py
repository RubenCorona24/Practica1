# Calcular el promedio de iMC
peso =  float(input("introduce tu peso: "))
estatura = float(input('introduce tu estatura en centimetros: '))
alturaf = estatura*estatura
imc = peso/alturaf
print('tu imc es de', imc)
if imc <= 18.5:
    print("tu imc es muy bajo")
elif imc > 25:
    print("tu imc es muy alto")

