from business.transaction_logic import transactionLogic
from decimal import Decimal,InvalidOperation
from os import system,name

class walletCollector():
    def __init__(self,user):
        self.tl=transactionLogic(user)

    def create_account(self,curr):
        try:
            self.tl.createAccount(curr)
            system('cls' if name == 'nt' else 'clear')
            print("\033[92mCuenta creada con éxito\033[0m")
        except ValueError as e:
            print("\033[91mERROR: {}\033[0m".format(e))

    def deposit_amount(self,amt):
        try:
            amount=Decimal(amt)
            self.tl.depositAmount(amount,"ARS")
            system('cls' if name == 'nt' else 'clear')
            print("\033[92mDepósito exitoso\033[0m")
        except InvalidOperation:
            print("\033[91mERROR: El valor ingresado es inválido\033[0m")
        except ValueError as e:
            print("\033[91mERROR: {}\033[0m".format(e))

    def purchase_currency(self,curr,amt):
        try:
            amount=Decimal(amt)
            self.tl.exchangeCurrency("ARS",curr,amount,"compra")
        except InvalidOperation:
            print("\033[91mERROR: El valor ingresado es inválido\033[0m")
        except ValueError as e:
            print("\033[91mERROR: {}\033[0m".format(e))

    def sell_currency(self,curr,amt):
        try:
            amount=Decimal(amt)
            self.tl.exchangeCurrency(curr,"ARS",amount,"venta")
        except InvalidOperation:
            print("\033[91mERROR: El valor ingresado es inválido\033[0m")
        except ValueError as e:
            print("\033[91mERROR: {}\033[0m".format(e))

        