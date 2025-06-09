from presentation.dataCollector import dataCollector
from presentation.secondary_menu import menuWallet

class Menu:
    def __init__(self):
        pass

    def showMenu(self):
        while True:
            print("-----------------------------------------------")
            print("1. Registrarse\n2. Iniciar Sesión\n0. Salir")
            op=input("Digite una opcion: ")
            print("-----------------------------------------------")
            match op:
                case "1":
                    dc=dataCollector(True)
                    dc.registration()
                case "2":
                    dc=dataCollector(False)
                    if dc.login():
                        m=menuWallet(dc.user)
                        m.showMenu()
                case "0":
                    print("\nFIN")
                    break
                case _:
                    print("\033[91m\nIngreso inválido\033[0m")