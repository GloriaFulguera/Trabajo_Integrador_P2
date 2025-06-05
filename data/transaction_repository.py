from data.data_helper import data_helper
from os.path import exists

class transactionRepository:
    def __init__(self):
        self.dh=data_helper()

    def create_account(self,user):
        userFile='data/accounts/{}.json'.format(user)

        if not exists(userFile):
            self.dh.serialize({"ARS":"0.00"},userFile)