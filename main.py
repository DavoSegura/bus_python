# from options import 
from bus import Bus
from options import CrearBus, ComprarBilletes, DevolverBilletes, CapacidadesBus
from usuario import Usuario
from login import *

run_app = False
usuario_admin = Usuario("admin","admin","admin@buspy.com")
usuarios = [usuario_admin]

isSesionIniciada = False
while isSesionIniciada == False:
    print("1.- Iniciar sesión\n2.- Registrarse\n")
    seleccion_menu_login = input()
    if seleccion_menu_login == '1':
        run_app = IniciarSesion(usuarios)
        print("Inicio de sesión correcto\n")
        isSesionIniciada = True
    elif seleccion_menu_login == '2':
        usuarios.append(Registro())
        print("Su usuario ha sido creado. Inicie sesión.\n")
    else:
        print("Error: Selección no es válida")

buses = []
CrearBus(buses)

while run_app == True:
        menu = '\n1.- Venta de billetes.\n2.- Devolución de billetes.\n3.- Estado de la venta.\n4.- Añadir bus\n0.- Salir.\n'
        print(menu)
        option = input("Selecciona un número: ")
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
