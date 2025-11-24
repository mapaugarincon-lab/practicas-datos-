from gestionar_persona import registrar_persona, consultar_persona , editar_persona , eliminar_usuario

while True:
    print("--------------- MENÚ ---------------")
    print("1. Registrar persona")
    print("2. Consultar persona")
    print("3. editar persona")
    print("4.eliminar persona")
    print("5.salir")
    print("------------------------------------")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_persona()
    elif opcion == "2":
        consultar_persona()
    elif opcion == "3":
        editar_persona()
    elif opcion == "4":
        eliminar_usuario()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")