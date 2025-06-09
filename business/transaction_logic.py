from data.transaction_repository import transactionRepository
from business.control_transaction import CheckCurrency,CheckAccountExists,CheckAccount,CheckAmount,CheckApiResponse,CheckBalance
import time

class transactionLogic:
    def __init__(self,user):
        self.user=user
        self.repo=transactionRepository(user)

    def createAccount(self,curr):
        controls=CheckCurrency(curr,self.user)
        controls.setNext(CheckAccountExists(curr,self.user))
        controls.handle(curr)

        self.repo.create_account(curr)

    def depositAmount(self,amt,acc):
        control=CheckAmount(amt)
        control.handle(amt)

        self.repo.credit_account(amt,acc)

    def exchangeCurrency(self,org,dst,amt,modo):
        lts=self.repo.get_rates()

        controls=CheckAccount(org,self.user)
        controls.setNext(CheckAccount(dst,self.user))\
        .setNext(CheckAmount(amt))\
        .setNext(CheckApiResponse(lts))
        controls.handle(org)

        if modo=="compra":
            total=self.getTotalPurchase(self.repo.get_rate(org,lts),self.repo.get_rate(dst,lts),amt)
            opControl=CheckBalance(total,self.repo.get_balance(org))
            opControl.handle(total)

            tinicio=time.time()
            rta = input("\033[93m\n¿Está seguro de que desea continuar con la operación? (S/N)\n\033[0m")
            if (time.time()-tinicio)>120:
                rta="N"
            if rta in("S","s"):
                self.repo.complete_exchange(org,dst,amt,total)
                print("\033[92mOperación realizada con éxito\033[0m")

            else:
                print("\033[91mOperación cancelada\033[0m")

        if modo=="venta":
            total=self.getTotalSell(self.repo.get_rate(org,lts),self.repo.get_rate(dst,lts),amt)
            opControl=CheckBalance(amt,self.repo.get_balance(org))
            opControl.handle(amt)

            tinicio=time.time()
            rta = input("\033[93m\n¿Está seguro de que desea continuar con la operación? (S/N)\n\033[0m")
            if (time.time()-tinicio)>120:
                rta="N"
            if rta in("S","s"):
                self.repo.complete_exchange(org,dst,total,amt)
                print("\033[92mOperación realizada con éxito\033[0m")

            else:
                print("\033[91mOperación cancelada\033[0m")
            
    def getTotalPurchase(self,rateOrg,rateDst,amt):
        total=(rateOrg/rateDst)*amt      
        return total
    
    def getTotalSell(self,rateOrg,rateDst,amt):
        total=(rateDst/rateOrg)*amt      
        return total