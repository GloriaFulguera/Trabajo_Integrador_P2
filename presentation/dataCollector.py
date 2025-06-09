from business.user_logic import userLogic
from getpass import getpass
from os import system,name

class dataCollector:
    def __init__(self,reg):#registro? registration :login
        if reg:
            self.user=input("Usuario: ").strip()
            self.password=getpass("Contraseña: ")
            self.vPassword=getpass("Reingrese la contraseña: ")
        else:
            self.user=input("Usuario: ")
            self.password=getpass("Contraseña: ")

    def registration(self):
        logica=userLogic(self.user,self.password,self.vPassword)
        try:
            logica.register()
            system('cls' if name == 'nt' else 'clear')
            print("\033[92m\nRegistro exitoso\033[0m")
        except ValueError as e:
            print("\033[91mERROR: {}\033[0m".format(e))

    def login(self):
        logica=userLogic(self.user,self.password)
        try:
            logica.login()
            system('cls' if name == 'nt' else 'clear')
            print("\nBienvenido/a ",self.user)
            return True
                        
        except ValueError as e:
            print("\033[91mERROR: {}\033[0m".format(e))
            return False
    