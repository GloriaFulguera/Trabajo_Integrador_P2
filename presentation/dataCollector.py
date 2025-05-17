from business.user_logic import userLogic
from getpass import getpass

class dataCollector:
    def __init__(self,reg):#registro? registration :login
        if reg:
            self.user=input("Usuario: ")
            self.password=getpass("Contraseña: ")
            self.vPassword=getpass("Reingrese la contraseña: ")
        else:
            self.user=input("Usuario: ")
            self.password=getpass("Contraseña: ")

    def registration(self):
        logica=userLogic(self.user,self.password,self.vPassword)
        try:
            logica.validations(self.user,self.password,self.vPassword)
            logica.register()
            print("\nRegistro exitoso")
        except ValueError as e:
            print("ERROR: ",e)

    def login(self):
        logica=userLogic(self.user,self.password)
        try:
            logica.loginValidate()
            print("\nBienvenido de vuelta ",self.user)
        except ValueError as e:
            print("ERROR: ",e)
    