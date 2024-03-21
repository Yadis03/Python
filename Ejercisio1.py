class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Muy buenos días, mi nombre es: {self.__nombre}"

class Instituto:
    def __init__(self, NombreU):
        self.NombreU = NombreU

    def getUniversidad(self):
        return f"en {self.NombreU}"

class Estudiante(Persona, Instituto):
    __count = 0

    def __init__(self, nombre, edad, carrera, NombreU):
        Persona.__init__(self, nombre, edad)  
        Instituto.__init__(self, NombreU)  
        self.__carrera = carrera
        Estudiante.__count += 1

    def saludar(self):
        return f"{super().saludar()} Tengo {self.edad} y estudio {self.__carrera} {super().getUniversidad()}"

    @staticmethod
    def getContadorDeEstudiantes():
        return f"Se han creado {Estudiante.__count} estudiantes"

estudiante = Estudiante("Juan", 20, "Ingeniería", "Universidad de Cundinamarca")
estudiante2 = Estudiante("albicio", 24, "Enfermería", "Universidad Minuto de Dios")
print(estudiante.saludar())
print(estudiante2.saludar())
print(Estudiante.getContadorDeEstudiantes())


#Alba Yadira Nova Sierra
#jhonnyer Yampier Fresneda Malaver