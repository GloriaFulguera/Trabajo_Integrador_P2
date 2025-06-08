from data.transaction_repository import transactionRepository

class transactionLogic:
    def __init__(self,user):
        self.user=user
        self.repo=transactionRepository(user)

    def create_account(self,curr):
        if self.repo.account_exists(curr):
            raise ValueError("La cuenta ya existe")
        self.repo.create_account(curr)