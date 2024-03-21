class Bebida:
    def __init__(self, nombre):
        self.__nombre = nombre

    def getNombreBebida(self):
        return f"La bebida es {self.__nombre}"
    
class Producto:
    def __init__(self, costo, precio):
        self.costo = costo
        self.precio = precio
    
    def getGanancia(self):
        return f"la ganacia es: {self.precio - self.costo}"

class Cerveza(Bebida, Producto):

    __Count = 0

    def __init__(self, nombre, marca, alcohol, costo, precio):
        Bebida.__init__(self, nombre)
        Producto.__init__(self, costo, precio)
        self.__marca = marca
        self.__alcohol = alcohol
        Cerveza.__Count += 1
    
    def getNombreBebida(self):
        return f"{super().getNombreBebida()} de la marca {self.__marca} con grado de alchohol {self.__alcohol} grados"
    
    def saludarComensal(self, nombre, edad):

        if edad < 18:
            return f"Hola {nombre} tu edad es {edad} no debes berberme"
        else:
            return f"Hola {nombre} el exceso de alcohol es perjudicial para la salud"


    @staticmethod
    def getContadorDeCervezas():
        return f"se han creado {Cerveza.__Count} cervezas"

cerveza = Cerveza("Poker", "Bavaria", 4.0, 1500, 2000)
cerveza2 = Cerveza("Aguila","Bavaria", 4.0, 1400, 2000)
print(cerveza.getNombreBebida())
print(cerveza.getGanancia())
print(cerveza2.getNombreBebida())
print(cerveza2.getGanancia())
print(cerveza2.saludarComensal("Diego", 28))


print(Cerveza.getContadorDeCervezas())

# bedida = Bebida("Jugo de mora")
# print(bedida.getNombreBebida())
