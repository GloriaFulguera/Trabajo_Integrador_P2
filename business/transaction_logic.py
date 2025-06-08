from data.transaction_repository import transactionRepository

class transactionLogic:
    def __init__(self,user):
        self.user=user
        self.repo=transactionRepository(user)

    def create_account(self,curr):
        if not self.repo.rate_exists(curr):
            raise ValueError("Codigo de divisa invalido")
        if self.repo.account_exists(curr):
            raise ValueError("La cuenta ya existe")
        self.repo.create_account(curr)

    def depositAmount(self,amt,acc):
        if amt<=0:
            raise ValueError("No se puede operar con el monto ingresado")
        self.repo.credit_account(amt,acc)