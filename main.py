class Persona():
    nombre = ""
    edad = 0
    dni = ""

    def __init__(self, nombre = "", edad = 0, dni = ""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def getNombre(self):
        return print(self.nombre)
    def getEdad(self):
        return print(self.edad)
    def getDNI(self):
        return print(self.dni)

    def setNombre(self, x):
        self.nombre = x
    def setEdad(self, x):
        self.edad = x
    def setDNI(self, x):
        self.dni = x

    def muestraDatos(self):
        return print("Datos de la persona:\nNombre: ",self.nombre,"\nEdad: ",self.edad,"\nDNI: ",self.dni)

    def esMayorEdad(self, x):
        if (x >= 18):
            return print(True)
        else:
            return print(False)

nombre = str(input("Introduce el nombre: "))
edad = int(input("Introduce la edad: "))
dni = str(input("Introduce el DNI:"))

alvaro = Persona

alvaro.setNombre = nombre
alvaro.setEdad = edad
alvaro.setDNI = dni

alvaro.muestraDatos
