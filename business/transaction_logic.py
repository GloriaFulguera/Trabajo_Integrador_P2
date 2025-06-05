from data.transaction_repository import transactionRepository

class transactionLogic:
    def __init__(self,user):
        self.user=user
        self.repo=transactionRepository()
        self.repo.create_account(self.user)
