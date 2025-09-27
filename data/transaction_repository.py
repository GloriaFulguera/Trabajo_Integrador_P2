import sqlobject as SO
from os import getenv
from requests import get
from dotenv import load_dotenv
from decimal import Decimal
from data.data_repository import Usuarios

load_dotenv()
__connection__=SO.connectionForURI(getenv("DATABASE"))

class Monedas(SO.SQLObject):
    class sqlmeta:
        table="monedas"
        idName="codigo"
        idType=str
    codigo=SO.StringCol(length=3, varchar=True)
    nombre=SO.StringCol(length=100, varchar=True)
    cuentas=SO.MultipleJoin('Cuentas', joinColumn='id_moneda')

class Cuentas(SO.SQLObject):
    id_usuario=SO.ForeignKey('Usuarios',default=None,cascade=True,dbName='id_usuario')
    id_moneda=SO.ForeignKey('Monedas',default=None,cascade=True,dbName='id_moneda')
    saldo=SO.DecimalCol(size=(10,2),precision=2)


class transactionRepository:
    def __init__(self,user):
        self.user=user
        self.create_account_default()

    def get_rates(self):
        rates=None
        response=get("https://api.currencyfreaks.com/v2.0/rates/latest?apikey={}".format(getenv("API_KEY")))
        if response.status_code==200:
            data=response.json()
            rates=data["rates"]

        return rates
    
    def create_account_default(self):
        try:
            user=Usuarios.selectBy(usuario=self.user).getOne()
            curr=Monedas.selectBy(codigo='ARS').getOne()
            Cuentas.select(SO.AND(Cuentas.q.id_usuario==user.id,Cuentas.q.id_moneda==curr.codigo)).getOne()
        except SO.SQLObjectNotFound:
            Cuentas(id_usuario=user.id, id_moneda=curr.codigo, saldo=0)

    def create_account(self,p_curr):
        try:
            user=Usuarios.selectBy(usuario=self.user).getOne()
            curr=Monedas.selectBy(codigo=p_curr).getOne()
            Cuentas(id_usuario=user.id, id_moneda=curr.codigo, saldo=0)
        except SO.SQLObjectNotFound:
            raise ValueError("Ocurrio un error en create_account, contacte al administrador")

    def account_exists(self,p_curr):
        try:
            user=Usuarios.selectBy(usuario=self.user).getOne()
            Cuentas.select(SO.AND(Cuentas.q.id_usuario==user.id,Cuentas.q.id_moneda==p_curr)).getOne()
            return True
        except SO.SQLObjectNotFound:
            return False
        
    def rate_exists(self,p_rate):
        try:
            Monedas.selectBy(codigo=p_rate).getOne()
            return True
        except SO.SQLObjectNotFound:
            return False
        
    def credit_account(self,p_amt,p_acc):
        try:
            user=Usuarios.selectBy(usuario=self.user).getOne()
            acc=Cuentas.select(SO.AND(Cuentas.q.id_usuario==user.id,Cuentas.q.id_moneda==p_acc)).getOne()
            value= acc.saldo+p_amt
            acc.saldo=value
        except SO.SQLObjectNotFound:
            raise ValueError("Ocurrio un error en credit_account, contacte al administrador")

    def get_balance(self,p_acc):
        try:
            user=Usuarios.selectBy(usuario=self.user).getOne()
            acc=Cuentas.select(SO.AND(Cuentas.q.id_usuario==user.id,Cuentas.q.id_moneda==p_acc)).getOne()
            return acc.saldo
        except SO.SQLObjectNotFound:
            raise ValueError("Ocurrio un error en get_balance, contacte al administrador")
    
    def get_rate(self,curr,rates):
        return Decimal(rates[curr])

    def complete_exchange(self,p_org,p_dst,p_deposit,p_withdraw):
        try:
            user=Usuarios.selectBy(usuario=self.user).getOne()
            accountOrg=Cuentas.select(SO.AND(Cuentas.q.id_usuario==user.id,Cuentas.q.id_moneda==p_org)).getOne()
            accountDst=Cuentas.select(SO.AND(Cuentas.q.id_usuario==user.id,Cuentas.q.id_moneda==p_dst)).getOne()
            discount=accountOrg.saldo-p_withdraw
            credit= accountDst.saldo+p_deposit

            accountOrg.saldo=discount
            accountDst.saldo=credit
        except SO.SQLObjectNotFound:
            raise ValueError("Ocurrio un error en complete_exchange, contacte al administrador")

