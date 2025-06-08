from presentation.walletCollector import walletCollector

class menuWallet:
    def __init__(self,user):
        self.wc=walletCollector(user)

    def showMenu(self):
        while True:
            print("-----------------------------------------------")
            print("1. Crear cuenta\n2. Comprar moneda\n3. Vender moneda\n4. Depositar ARS\n0. Salir")
            op=input("Digite una opcion: ")
            print("-----------------------------------------------")
            match op:
                case "1":
                    value=input("Ingrese moneda: ")
                    self.wc.create_account(value.strip().upper())
                case "2":
                    break
                case "3":
                    break
                case "4":
                    value=input("Ingrese monto a depositar: ")
                    self.wc.deposit_amount(value.strip())
                case "0":
                    print("\nFIN")
                    break
                case _:
                    print("\nIngreso no valido")