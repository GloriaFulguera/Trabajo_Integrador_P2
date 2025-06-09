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
            print("Cuenta creada con éxito")
        except ValueError as e:
            print("ERROR: ",e)

    def deposit_amount(self,amt):
        try:
            amount=Decimal(amt)
            self.tl.depositAmount(amount,"ARS")
            system('cls' if name == 'nt' else 'clear')
            print("Depósito exitoso")
        except InvalidOperation:
            print("ERROR: El valor ingresado no es valido")
        except ValueError as e:
            print("ERROR: ",e)

    def purchase_currency(self,curr,amt):
        try:
            amount=Decimal(amt)
            self.tl.exchangeCurrency("ARS",curr,amount,"compra")
        except InvalidOperation:
            print("ERROR: El valor ingresado no es valido")
        except ValueError as e:
            print("ERROR: ",e)

    def sell_currency(self,curr,amt):
        try:
            amount=Decimal(amt)
            self.tl.exchangeCurrency(curr,"ARS",amount,"venta")
        except InvalidOperation:
            print("ERROR: El valor ingresado no es valido")
        except ValueError as e:
            print("ERROR: ",e)

        