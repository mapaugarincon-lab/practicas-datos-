class Agregar:
    def __init__(self, nombre, cedula, edad):
        self._nombre = nombre
        self._cedula = cedula
        self._edad = edad

def agregar_persona():
    print("--- Agregar Persona ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    cedula = input("Cédula: ")

    p = Agregar(nombre, edad, cedula)
    personas = []  
    personas.append(p)
    print("Persona agregada con éxito.")