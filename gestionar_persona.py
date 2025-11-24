from personas import Persona

def registrar_persona():
    print("--- Registrar Persona ---")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    cedula = input("Cédula: ")
    ciudad = input("Ciudad: ")
    correo = input("Correo: ")

    nueva_persona = Persona(nombre, edad, cedula, ciudad, correo)
    Persona.personas.append(nueva_persona)

    print("Persona registrada con éxito\n")


def consultar_persona():
    print("--- Consultar Persona ---")
    cedula_buscar = input("Ingrese la cédula: ")

    for p in Persona.personas:
        if p.cedula == cedula_buscar:
            print("Persona encontrada:")
            print(p, "\n")
            return

    print("Persona no encontrada\n")


def eliminar_usuario():
    print("--- Eliminar Persona ---")
    cedula_buscar = input("Ingrese la cédula a eliminar: ")

    for p in Persona.personas:
        if p.cedula == cedula_buscar:
            Persona.personas.remove(p)
            print("Persona eliminada.\n")
            return

    print("Persona no encontrada.\n")


def editar_persona():
    print("--- Editar Persona ---")
    cedula_buscar = input("Ingrese la cédula de la persona a editar: ")

    for p in Persona.personas:
        if p.cedula == cedula_buscar:
            nuevo_nombre = input("Nuevo nombre (Enter para no cambiar): ")
            if nuevo_nombre:
                p.nombre = nuevo_nombre

            nueva_edad = input("Nueva edad (Enter para no cambiar): ")
            if nueva_edad:
                p.edad = nueva_edad

            nueva_ciudad = input("Nueva ciudad (Enter para no cambiar): ")
            if nueva_ciudad:
                p.ciudad = nueva_ciudad

            nuevo_correo = input("Nuevo correo (Enter para no cambiar): ")
            if nuevo_correo:
                p.correo = nuevo_correo

            print("Datos actualizados.\n")
            return

    print("Persona no encontrada.\n")
