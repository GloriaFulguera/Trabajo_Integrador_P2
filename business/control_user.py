from business.cor import BaseHandler
from data.data_repository import UserRepository
from re import match

###VALIDACIONES DE REGISTRO
class CheckEmpty(BaseHandler):
    def __init__(self,user,pwd):
        self.user=user
        self.pwd=pwd

    def handle(self, user):
        if not(self.user=="" or self.pwd==""):
            return super().handle(user)
        else:
            raise ValueError("Ningun campo puede estar vacio")
        
class CheckUsername(BaseHandler):
    def __init__(self,user):
        self.user=user

    def handle(self, user):
        if len(self.user)>4:
            return super().handle(user)
        else:
            raise ValueError("Nombre de usuario demasiado corto")
        
class CheckStrongPassword(BaseHandler):
    def __init__(self,pwd):
        self.pwd=pwd

    def handle(self, pwd):
        if len(self.pwd)>4:
            return super().handle(pwd)
        else:
            raise ValueError("Contrasenia demasiado corta")
        
class CheckPassword(BaseHandler):
    def __init__(self,pwd,pwd2):
        self.pwd=pwd
        self.pwd2=pwd2

    def handle(self, pwd):
        if self.pwd==self.pwd2:
            return super().handle(pwd)
        else:
            raise ValueError("Las contrasenias no coinciden")
        
class CheckUserExist(BaseHandler):
    def __init__(self,user):
        self.user=user
        self.ur=UserRepository()

    def handle(self, user):
        if not (self.ur.user_exists(self.user)):
            return super().handle(user)
        else:
            raise ValueError("El usuario ya existe")
        
###VALIDACIONES DE LOGIN
class CheckUser(BaseHandler):
    def __init__(self,user):
        self.user=user
        self.ur=UserRepository()

    def handle(self, user):
        if self.ur.user_exists(self.user):
            return super().handle(user)
        else:
            raise ValueError("Usuario o contrasenia invalida")
        
class CheckUserRegistry(BaseHandler):
    def __init__(self,user,pwd):
        self.user=user
        self.pwd=pwd
        self.ur=UserRepository()

    def handle(self, user):
        if self.ur.user_valid(self.user,self.pwd):
            return super().handle(user)
        else:
            raise ValueError("Usuario o contrasenia invalida")