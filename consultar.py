class consultar_persona:
    print("Consultar Persona")
    cedula = input("Cédula: ")

    personas = []  
    for p in personas:
        if p.cedula == cedula:
            print("Persona encontrada:")
            print(p, "cedula")
         

print("No existe una persona con esa cédula.")