from persona import Persona

def consultar_persona():
    print("--- Consultar Persona ---")
    cedula_buscar = input("Ingrese la cédula: ")

    for p in Persona.personas:
        if p.cedula == cedula_buscar:
            print("\n✔ Persona encontrada:")
            print(p, "\n")
            return
    
    print(" Persona no encontrada")