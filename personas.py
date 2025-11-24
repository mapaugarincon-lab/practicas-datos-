class Persona :
    personas=[]
    def __init__(self, nombre, edad, cedula, ciudad, correo):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.ciudad = ciudad 
        self.correo = correo

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
    @property 
    def ciudad(self):
        return self._ciudad
    @ciudad.setter 
    def ciudad(self,ciudad):
        self._ciudad = ciudad 
    @property
    def correo(self):
        return self._correo 
    @correo.setter 
    def correo(self,correo):
        self._correo = correo  


    def __str__(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Cédula: {self._cedula}, Ciudad: {self._ciudad}, Correo: {self._correo}"