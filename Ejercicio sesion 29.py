class Persona :

    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.edad=edad

    def getSaludar(self):
        return f"Buenos dias mi nombre es {self.__nombre}"
    
class Estudiante(Persona):

    __Count = 0

    def __init__(self,nombre,edad,carrera):
        super().__init__(nombre,edad)
        self.__carrera=carrera
        Estudiante.__Count += 1

    def getSaludar(self):
        return f"{super().getSaludar()} tengo una edad {self.__edad} de la carrera{self.__carrera}"
    
estudiante=Estudiante("Alba",25,"Ingenieria de sistemas")
print(estudiante.getSaludar())

@staticmethod
def ContarEstudiantes():
    return f"se han creado {Estudiante.__Count} estudiantes"

