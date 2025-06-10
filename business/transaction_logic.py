from data.transaction_repository import transactionRepository
from business.control_transaction import CheckCurrency,CheckAccountExists,CheckAccount,CheckAccounts,CheckAmount,CheckApiResponse,CheckBalance

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

    def validateExchange(self,org,dst,amt,modo):
        lts=self.repo.get_rates()

        controls=CheckAccount(org,self.user)
        controls.setNext(CheckAccount(dst,self.user))\
        .setNext(CheckAccounts(org,dst))\
        .setNext(CheckAmount(amt))\
        .setNext(CheckApiResponse(lts))
        controls.handle(org)

        if modo=="compra":
            total=self.getTotalPurchase(org,dst,amt,lts)
            opControl=CheckBalance(total,self.repo.get_balance(org))
            opControl.handle(total)

        if modo=="venta":
            total=self.getTotalSell(org,dst,amt,lts)
            opControl=CheckBalance(amt,self.repo.get_balance(org))
            opControl.handle(amt)
        return lts
            
    def completeExchange(self,org,dst,deposit,withdraw):
        self.repo.complete_exchange(org,dst,deposit,withdraw)
    
    def getTotalPurchase(self,rateOrg,rateDst,amt,lts):
        total=(self.repo.get_rate(rateOrg,lts)/self.repo.get_rate(rateDst,lts))*amt      
        return total
    
    def getTotalSell(self,rateOrg,rateDst,amt,lts):
        total=(self.repo.get_rate(rateDst,lts)/self.repo.get_rate(rateOrg,lts))*amt      
        return total