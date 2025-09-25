class Bus:
    def __init__(self, bCapacidad, destino):
        self.setCapacidad(bCapacidad)
        self.__billetes_vendidos = []
        self.__billetes_disponibles = bCapacidad
        self.__destino = destino

    def getDestino(self):
        return self.__destino

    def setBilletesVendidos(self, isCompra, billete):
        if isCompra == True:
            self.__billetes_vendidos.append(billete)
        else:
            if billete in self.__billetes_vendidos:
                self.__billetes_vendidos.remove(billete)
            else:
                print("Error: Billete no encontrado")

    def setBilletesDisponibles(self, isCompra):
        if isCompra:
            self.__billetes_disponibles -= 1
        else:
            self.__billetes_disponibles += 1

    def setCapacidad(self, bCapacidad):
        self.__capacidad = bCapacidad

    def getCapacidad(self):
        return self.__capacidad
    
    def getBilletesVendidos(self):
        return self.__billetes_vendidos
    
    def getBilletesDisponibles(self):
        return self.__billetes_disponibles