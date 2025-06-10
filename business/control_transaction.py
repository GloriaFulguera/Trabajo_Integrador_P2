from business.cor import BaseHandler
from data.transaction_repository import transactionRepository

class CheckCurrency(BaseHandler):
    def __init__(self,curr,user):
        self.curr=curr
        self.repo=transactionRepository(user)

    def handle(self, curr):
        if self.repo.rate_exists(self.curr):
            return super().handle(curr)
        else:
            raise ValueError("Código de divisa inválido")
        
class CheckAccountExists(BaseHandler):
    def __init__(self,curr,user):
        self.curr=curr
        self.repo=transactionRepository(user)

    def handle(self, curr):
        if not self.repo.account_exists(self.curr):
            return super().handle(curr)
        else:
            raise ValueError("La cuenta ya existe")
        
class CheckAccount(BaseHandler):
    def __init__(self,curr,user):
        self.curr=curr
        self.repo=transactionRepository(user)

    def handle(self, curr):
        if self.repo.account_exists(self.curr):
            return super().handle(curr)
        else:
            raise ValueError("Cuenta inválida")
        
class CheckAccounts(BaseHandler):
    def __init__(self,org,dst):
        self.org=org
        self.dst=dst

    def handle(self, org):
        if self.org != self.dst:
            return super().handle(org)
        else:
            raise ValueError("No puede operar con la misma moneda")
        
class CheckAmount(BaseHandler):
    def __init__(self,amt):
        self.amt=amt

    def handle(self, amt):
        if self.amt>0:
            return super().handle(amt)
        else:
            raise ValueError("No se puede operar con el monto ingresado")
        
class CheckApiResponse(BaseHandler):
    def __init__(self,lts):
        self.lts=lts

    def handle(self, lts):
        if self.lts is not None:
            return super().handle(lts)
        else:
            raise ValueError("Ocurrió un error al consultar API")
        
class CheckBalance(BaseHandler):
    def __init__(self,total,blc):
        self.total=total
        self.blc=blc

    def handle(self, total):
        if self.blc>=self.total:
            return super().handle(total)
        else:
            raise ValueError("Saldo insuficiente para realizar la operación")