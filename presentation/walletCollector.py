from business.transaction_logic import transactionLogic
from decimal import Decimal,InvalidOperation

class walletCollector():
    def __init__(self,user):
        self.tl=transactionLogic(user)

    def create_account(self,curr):
        try:
            self.tl.createAccount(curr)
        except ValueError as e:
            print("ERROR: ",e)

    def deposit_amount(self,amt):
        try:
            amount=Decimal(amt)
            self.tl.depositAmount(amount,"ARS")
        except InvalidOperation:
            print("ERROR: El valor ingresado no es valido")
        except ValueError as e:
            print("ERROR: ",e)

    def purchase_currency(self,curr,amt):
        try:
            amount=Decimal(amt)
            self.tl.exchangeCurrency("ARS",curr,amount)
        except InvalidOperation:
            print("ERROR: El valor ingresado no es valido")
        except ValueError as e:
            print("ERROR: ",e)