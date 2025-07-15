from datetime import date

ARCHIVO = 'gastos.txt'
open('gastos.txt', 'w').close()
def registrar_datos():
    while True:
        elección = input(
            "\n📋 BIENVENIDO AL REGISTRO DE DATOS 📋\n"
            "1.- AGREGAR UN GASTO, MONTO, CATEGORÍA, DESCRIPCIÓN\n"
            "2.- VER TODOS LOS GASTOS\n"
            "3.- VER TOTAL GASTADO\n"
            "4.- SALIR\n"
            "RESPUESTA: "
        )

        if elección == '1':
            print("\n*** Has escogido la opción de agregar un gasto ***")
            try:
                monto = float(input("¿Cuánto es el monto gastado?: $"))
            except ValueError:
                print("❌ Error: Debes ingresar un número válido para el monto.")
                continue

            categoria = input("¿De qué categoría es? (comida, transporte, etc.): ")
            descripcion = input("Agrega una breve descripción: ")
            fecha_input = input("Fecha (YYYY-MM-DD) o presiona ENTER para usar la fecha de hoy: ")
            fecha = fecha_input if fecha_input else str(date.today())

            with open(ARCHIVO, 'a') as archivo:
                archivo.write(f"{monto}/{categoria}/{descripcion}/{fecha}\n")
            print("✅ Gasto registrado exitosamente.\n")

        elif elección == '2':
            print("\n*** Lista de todos los gastos registrados ***\n")
            print(f"{'Monto':<10} | {'Categoría':<15} | {'Descripción':<30} | Fecha")
            print("-" * 75)
            try:
                with open(ARCHIVO, 'r') as archivo:
                    for linea in archivo:
                        partes = linea.strip().split('/')
                        if len(partes) == 4:
                            print(f"${partes[0]:<9} | {partes[1]:<15} | {partes[2]:<30} | {partes[3]}")
            except FileNotFoundError:
                print("📁 No hay gastos registrados todavía.\n")

        elif elección == '3':
            print("\n*** Calculando el total de todos los gastos ***")
            total = 0
            try:
                with open(ARCHIVO, 'r') as archivo:
                    for linea in archivo:
                        partes = linea.strip().split('/')
                        if len(partes) >= 1:
                            try:
                                monto = float(partes[0].strip())
                                total += monto
                            except ValueError:
                                pass
                print(f"\n💵 Total gastado: ${total:.2f}\n")
            except FileNotFoundError:
                print("📁 No hay gastos registrados todavía.\n")

        elif elección == '4':
            print("👋 Has salido del registro de gastos. ¡Hasta pronto!")
            break

        else:
            print("❌ Opción no válida. Escribe 1, 2, 3 o 4.\n")

# Ejecutar el programa
registrar_datos()