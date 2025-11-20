class Persona:
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def cedula(self):
        return self._cedula
    @cedula.setter
    def cedula(self,cedula):
        self._cedula = cedula
    def __str__(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Cédula: {self._cedula}"
    
    personas=[]