from cliente import Cliente

class Billete:
    def __init__(self, cliente):
        self.setCliente(cliente)

    def getCliente(self):
        return self.__cliente

    def setCliente(self, cliente):
        self.__cliente = cliente