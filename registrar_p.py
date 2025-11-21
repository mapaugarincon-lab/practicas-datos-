from persona import Persona

def registrar_persona():
    print("--- Registrar Persona ---")

    nombre = input("Nombre: ")
    edad = input("Edad: ")
    cedula = input("Cédula: ")
    ciudad = input("Ciudad: ")
    correo = input("Correo: ")

    nueva_persona = Persona(nombre, edad, cedula, ciudad, correo)
    Persona.personas.append(nueva_persona)

    print(" Persona registrada con éxito")