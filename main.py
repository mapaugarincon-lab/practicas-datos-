from persona import Persona
from registrar_p import registrar_persona
from consultar import consultar_persona
from agregar import agregar_persona



while True:
    print("-------------------------------------MENÚ---------------------------------")
    print("1. Registrar persona")
    print("2. consultar")
    print("3. agregar")
    print("4. salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
            registrar_persona()
    elif opcion == "2":
            consultar_persona()
    elif opcion == "3":
            agregar_persona()
    elif opcion == "4":
            print("Saliendo...")
            break
    else:
            print("Opción inválida")
            
   