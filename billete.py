from bus import Bus

class Billete:
    def __init__(self, bus):
        self.__bus = bus

    def getBus(self):
        return self.__bus