from usuario import Usuario

def IniciarSesion(usuarios):
    successful_login = False

    while successful_login == False:
        username = input("Introduce el usuario: ")
        password = input("Introduce la contraseña: ")

        for usuario in usuarios:
            if usuario.getUsername() == username and usuario.getPassword() == password:
                successful_login = True
                
        if successful_login == False:
            print("Usuario o contraseña incorrectos. Intenta de nuevo.")

    return successful_login

def Registro():
    username = input("Introduce el nombre de usuario: ")
    password = input("Introduce la contraseña: ")
    email = input("Introduce el correo electrónico: ")

    usuario_nuevo = Usuario(username, password, email)
    return usuario_nuevo