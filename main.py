# from options import 
from bus import Bus
from options import CrearBus, ComprarBilletes, DevolverBilletes, CapacidadesBus

buses = []
CrearBus(buses)

run_app = True
while run_app == True:
        menu = '\n1.- Venta de billetes.\n2.- Devolución de billetes.\n3.- Estado de la venta.\n4.- Añadir bus\n0.- Salir.'
        print(menu)
        option = input()
        if option == '1':
            print(ComprarBilletes(buses))
        elif option == '2':
            
            print(DevolverBilletes(buses))
        elif option == '3':
            
            print(CapacidadesBus(buses))
        elif option == '4':
            CrearBus(buses)

        elif option == '0':
            run_app = False
        else:
            print('Error. Introduce un numero del menu.')
