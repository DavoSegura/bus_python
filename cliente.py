class Cliente:
    def __init__(self, nombre, apellido):
        self.setNombre(nombre)
        self.setApellido(apellido)

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido