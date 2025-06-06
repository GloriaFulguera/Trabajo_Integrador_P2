from data.data_helper import data_helper
from os.path import exists

class transactionRepository:
    def __init__(self,user):
        self.user=user
        self.dh=data_helper()
        self.userFile='data/accounts/{}.json'.format(self.user)

        if not exists(self.userFile):
            self.dh.serialize({"ARS":"0.00"},self.userFile)

    def create_account(self,curr):
        accs=self.dh.deserialize(self.userFile)
        accs[curr]="0.00"
        self.dh.serialize(accs,self.userFile)

    def account_exists(self,curr):
        accs=self.dh.deserialize(self.userFile)
        if curr in accs:
            return True
        else:
            return False