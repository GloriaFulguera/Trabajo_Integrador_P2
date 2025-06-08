from data.data_helper import data_helper
from os.path import exists
from os import makedirs,getenv
from requests import get
from dotenv import load_dotenv

class transactionRepository:
    def __init__(self,user):
        self.user=user
        self.dh=data_helper()
        self.userFile='data/accounts/{}.json'.format(self.user)

        if not exists("data/accounts"):
            makedirs("data/accounts")

        if not exists(self.userFile):
            self.dh.serialize({"ARS":"0.00"},self.userFile)
        load_dotenv()
        self.get_rates()

    def get_rates(self):
        if not exists("data/rates.json"):
            print("gaste una peticion")
            response=get("https://api.currencyfreaks.com/v2.0/rates/latest?apikey={}".format(getenv("API_KEY")))

            if response.status_code==200:
                data=response.json()
                rates=data["rates"]
                self.dh.serialize(rates,"data/rates.json")

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