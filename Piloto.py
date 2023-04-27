class Piloto:
    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__fechaNacimiento = None
        self.__pais = None
        self.__salarioAnual = None

    @property 
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato

    @property 
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, dato):
        self.__apellido = dato

    @property 
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    
    @fechaNacimiento.setter
    def fechaNacimiento(self, dato):
        self.__fechaNacimiento = dato

    @property 
    def pais(self):
        return self.__pais
    
    @pais.setter
    def pais(self, dato):
        self.__pais = dato

    @property 
    def salarioAnual(self):
        return self.__salarioAnual

    @salarioAnual.setter
    def salarioAnual(self, dato):
        self.__salarioAnual = dato
