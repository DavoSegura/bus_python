class Usuario:
    def __init__(self, username, password, email):
        self.setUsername(username)
        self.setPassword(password)
        self.setEmail(email)
        
    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def setEmail(self, email):
        self.__email = email

    def getUsername(self):
        return self.__username
    
    def getPassword(self):
        return self.__password
    
    def getEmail(self):
        return self.__email
