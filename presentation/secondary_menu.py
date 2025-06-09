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
                    valueCur=input("Ingrese la moneda que desea comprar: ")
                    value=input("Ingrese la cantidad que desea comprar: ")
                    self.wc.purchase_currency(valueCur.strip().upper(),value)
                case "3":
                    valueCur=input("Ingrese la moneda que desea vender: ")
                    value=input("Ingrese la cantidad que desea vender: ")
                    self.wc.sell_currency(valueCur.strip().upper(),value)
                case "4":
                    value=input("Ingrese monto a depositar: ")
                    self.wc.deposit_amount(value.strip())
                case "0":
                    print("\nFIN")
                    break
                case _:
                    print("\033[91m\nIngreso inválido\033[0m")