def iniciar():
    #agenda
    agenda = {"Roberto":"3434334"}
    print("Tienes 5 opciones en esta agenda:\n1.-Añadir un contacto\n2.-Buscar un contacto\n3.-Editar un contacto\n4.-Eliminar un contacto\n5.-Mostrar todos los contatos")
    eleccion = int(input("¿Qué opción eliges?: "))
    if eleccion ==1:
        print("Claro, añade un nuevo contacto")
        name = input("Nombre del contacto: ")
        num = int(input("Número del contacto: "))
        if name and num:
            agenda.update({name:num}) 
            print(F"Se há modificado la agenda: {agenda}")
        else:
            print("No has ingresado nada")
    elif eleccion ==2:
        print("Claro, te vamos a buscar un contacto")
        name = input("Nombre de tu contacto: ")
        if name  in agenda:
            print(f"Encontramos a tu contacto {name} de número {agenda[name]}")
        else:
            print("ERROR, no se encontró tu contacto en la agenda")
    elif eleccion==3:
        print("Claro, vamos a editar un contacto ")
        name = input("Nombre del contacto: ")
        if name in agenda:
            new_phone = input("Introduzca el nuevo teléfono: ")
            agenda.update({name,new_phone})
            print(F"Se ha modificado el número a: {agenda[name]}")
        else:
            print("ERROR, contacto no existente en tu agenda")
    elif eleccion==4:
        print("Claro, vamos a eliminar un contacto")
        name = input("Nombre del contacto: ")
        if name in agenda:
            eliminado = agenda.pop(name)
            print(F"El contacto eliminado en la agenda fue de {eliminado}")
        else:
            print("ERROR, contacto no existente en tu agenda")
    elif eleccion==5:
        print("Claro, te mostramos todos los contactos: ")
        print(agenda)
    else:
        print("ERROR, opción inválida")
iniciar()