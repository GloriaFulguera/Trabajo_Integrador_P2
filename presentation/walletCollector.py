from business.transaction_logic import transactionLogic
from decimal import Decimal,InvalidOperation
from os import system,name
import time

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
            ltsRates=self.tl.validateExchange("ARS",curr,amount,"compra")

            tinicio=time.time()
            rta = input("\033[93m\n¿Está seguro de que desea continuar con la operación? (S/N)\n\033[0m")
            if (time.time()-tinicio)>10:
                rta="N"
            if rta in("S","s"):
                self.tl.completeExchange("ARS",curr,amount,self.tl.getTotalPurchase("ARS",curr,amount,ltsRates))
                print("\033[92mOperación realizada con éxito\033[0m")
            else:
                print("\033[91mOperación cancelada\033[0m")

        except InvalidOperation:
            print("\033[91mERROR: El valor ingresado es inválido\033[0m")
        except ValueError as e:
            print("\033[91mERROR: {}\033[0m".format(e))

    def sell_currency(self,curr,amt):
        try:
            amount=Decimal(amt)
            ltsRates=self.tl.validateExchange(curr,"ARS",amount,"venta")

            tinicio=time.time()
            rta = input("\033[93m\n¿Está seguro de que desea continuar con la operación? (S/N)\n\033[0m")
            if (time.time()-tinicio)>10:
                rta="N"
            if rta in("S","s"):
                self.tl.completeExchange(curr,"ARS",self.tl.getTotalSell(curr,"ARS",amount,ltsRates),amount)
                print("\033[92mOperación realizada con éxito\033[0m")
            else:
                print("\033[91mOperación cancelada\033[0m")

        except InvalidOperation:
            print("\033[91mERROR: El valor ingresado es inválido\033[0m")
        except ValueError as e:
            print("\033[91mERROR: {}\033[0m".format(e))

        