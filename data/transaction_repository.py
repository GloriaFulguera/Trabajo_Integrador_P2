from data.data_helper import data_helper
from os.path import exists
from os import makedirs,getenv
from requests import get
from dotenv import load_dotenv
from decimal import Decimal

class transactionRepository:
    def __init__(self,user,archivo="data/rates.json"):
        self.user=user
        self.ratesFile=archivo
        self.dh=data_helper()
        self.userFile='data/accounts/{}.json'.format(self.user)

        if not exists("data/accounts"):
            makedirs("data/accounts")

        if not exists(self.userFile):
            self.dh.serialize({"ARS":"0.00"},self.userFile)
        load_dotenv()

    def get_rates(self):
        print("Gaste una req")
        rates=None
        rates=self.dh.deserialize(self.ratesFile)
        # response=get("https://api.currencyfreaks.com/v2.0/rates/latest?apikey={}".format(getenv("API_KEY")))
        # if response.status_code==200:
        #     data=response.json()
        #     rates=data["rates"]
        #     if not exists(self.ratesFile):
        #         print("GENERO EL JSON DE RATES")
        #         self.dh.serialize(rates,self.ratesFile)

        return rates

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
        
    def rate_exists(self,rate):
        rates=self.dh.deserialize(self.ratesFile)
        if rate in rates:
            return True
        else:
            return False
        
    def credit_account(self,amt,acc):
        accounts=self.dh.deserialize(self.userFile)
        value= Decimal(accounts[acc])+amt
        accounts[acc]=str(value)
        self.dh.serialize(accounts,self.userFile)

    def get_balance(self,acc):
        accounts=self.dh.deserialize(self.userFile)
        return Decimal(accounts[acc])
    
    def get_rate(self,curr,rates):
        return Decimal(rates[curr])

    def complete_exchange(self,org,dst,amt,tot):
        accounts=self.dh.deserialize(self.userFile)
        discount=Decimal(accounts[org])-Decimal(tot)
        credit=Decimal(accounts[dst])+Decimal(amt)
        accounts[org]=str(discount)
        accounts[dst]=str(credit)

        self.dh.serialize(accounts,self.userFile)
