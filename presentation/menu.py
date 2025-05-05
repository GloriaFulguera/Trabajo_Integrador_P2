from business.user_logic import userLogic
class dataCollector:
    def __init__(self):
        self.user=input("Usuario: ")
        self.password=input("Contraseña: ")

    def registrar(self):
        logica=userLogic(self.user,self.password)
        logica.registrar()
    