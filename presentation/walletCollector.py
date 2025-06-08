from business.transaction_logic import transactionLogic

class walletCollector():
    def __init__(self,user):
        self.tl=transactionLogic(user)

    def create_account(self,curr):
        try:
            self.tl.create_account(curr)
        except ValueError as e:
            print("ERROR: ",e)