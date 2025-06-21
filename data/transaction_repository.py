import sqlobject as SO
from data.data_helper import data_helper
from os.path import exists
from os import makedirs,getenv
from requests import get
from dotenv import load_dotenv
from decimal import Decimal

database='mysql://guest:1234@localhost/prog2'
__connection__=SO.connectionForURI(database)

class Usuarios(SO.SQLObject):
    usuario=SO.StringCol(length=100, varchar=True)
    clave=SO.StringCol(length=200,varchar=True)
    cuentas=SO.MultipleJoin('Cuentas', joinColumn='id_usuario')

class Monedas(SO.SQLObject):
    codigo=SO.StringCol(length=3, varchar=True)
    nombre=SO.StringCol(length=100, varchar=True)
    cuentas=SO.MultipleJoin('Cuentas', joinColumn='id_moneda')

class Cuentas(SO.SQLObject):
    id_usuario=SO.ForeignKey('Usuarios',default=None,cascade=True)
    id_moneda=SO.ForeignKey('Monedas',default=None,cascade=True)
    saldo=SO.DecimalCol(size=(10,2))


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
        rates=None
        response=get("https://api.currencyfreaks.com/v2.0/rates/latest?apikey={}".format(getenv("API_KEY")))
        if response.status_code==200:
            data=response.json()
            rates=data["rates"]
            if not exists(self.ratesFile):
                self.dh.serialize(rates,self.ratesFile)

        return rates

    def create_account(self,p_curr):
        # accs=self.dh.deserialize(self.userFile)
        # accs[curr]="0.00"
        # self.dh.serialize(accs,self.userFile)
        try:
            user=Usuarios.selectBy(usuario=self.user).getOne()
            curr=Monedas.selectBy(codigo=p_curr).getOne()
            Cuentas(id_usuario=user.id, id_moneda=curr.codigo, saldo=0)
        except SO.SQLObjectNotFound:
            raise ValueError("Ocurrio un error, contacte al administrador")

    def account_exists(self,p_curr):
        try:
            user=Usuarios.selectBy(usuario=self.user).getOne()
            Cuentas.select(SO.AND(Cuentas.q.id_usuario==user.id,Cuentas.q.id_moneda==p_curr))
            return True
        except SO.SQLObjectNotFound:
            return False
        # accs=self.dh.deserialize(self.userFile)
        # if curr in accs:
        #     return True
        # else:
        #     return False
        
    def rate_exists(self,p_rate):

        if not exists(self.ratesFile):
            self.get_rates()
        # rates=self.dh.deserialize(self.ratesFile)
        # if rate in rates:
        #     return True
        # else:
        #     return False
        
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

    def complete_exchange(self,org,dst,deposit,withdraw):
        accounts=self.dh.deserialize(self.userFile)
        discount=Decimal(accounts[org])-Decimal(withdraw)
        credit=Decimal(accounts[dst])+Decimal(deposit)
        accounts[org]=str(discount)
        accounts[dst]=str(credit)

        self.dh.serialize(accounts,self.userFile)
