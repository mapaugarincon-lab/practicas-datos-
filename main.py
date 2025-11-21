from registrar_p import registrar_persona
from consultar import consultar_persona


while True:
    print("--------------- MENÚ ---------------")
    print("1. Registrar persona")
    print("2. Consultar persona")
    print("3. Salir")
    print("------------------------------------")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_persona()
    elif opcion == "2":
        consultar_persona()
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")