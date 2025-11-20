

class Persona:
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula

class registrar_p:
        print("--- Registrar Persona ---")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        cedula = input("Cédula: ")

        p = Persona(nombre, edad, cedula)
        personas = []  
        personas.append(p)
        print("Persona registrada con éxito.")
    