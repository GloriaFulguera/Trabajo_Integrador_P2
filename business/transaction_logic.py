from data.transaction_repository import transactionRepository

class transactionLogic:
    def __init__(self,user):
        self.user=user
        self.repo=transactionRepository(user)

    def createAccount(self,curr):
        if not self.repo.rate_exists(curr):
            raise ValueError("Codigo de divisa invalido")
        if self.repo.account_exists(curr):
            raise ValueError("La cuenta ya existe")
        self.repo.create_account(curr)

    def depositAmount(self,amt,acc):
        if amt<=0:
            raise ValueError("No se puede operar con el monto ingresado")
        self.repo.credit_account(amt,acc)

    def exchangeCurrency(self,org,dst,amt):
        if not self.repo.account_exists(org):
            raise ValueError("Cuenta origen invalida")
        if not self.repo.account_exists(dst):
            raise ValueError("Cuenta destino invalida")
        if amt<=0:
            raise ValueError("No se puede operar con el monto ingresado")
        lts=self.repo.get_rates()
        if lts is None:
            raise ValueError("Ocurrio un error al consultar API")
        total=self.getTotal(self.repo.get_rate(org,lts),self.repo.get_rate(dst,lts),amt)
        if total > self.repo.get_balance(org):
            raise ValueError("Saldo insuficiente para realizar la operacion")
        self.repo.complete_exchange(org,dst,amt,total)
        
    def getTotal(self,rateOrg,rateDst,amt):
        total=(rateDst/rateOrg)*amt      
        return total