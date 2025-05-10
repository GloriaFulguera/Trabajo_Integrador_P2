from business.user_logic import userLogic
from getpass import getpass
class dataCollector:
    def __init__(self):
        self.user=input("Usuario: ")
        self.password=getpass("Contraseña: ")
        self.vPassword=getpass("Reingrese la contraseña: ")

    def registration(self):
        logica=userLogic(self.user,self.password,self.vPassword)
        try:
            logica.passwordValidate(self.password,self.vPassword)
            logica.register()
        except ValueError as e:
            print("ERROR: ",e)
    