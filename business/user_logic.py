from data.data_helper import data_helper
from data.data_repository import UserRepository

class userLogic:

    def __init__(self,user,pwd,vpwd=None):
        self.user=user
        self.pwd=pwd
        self.vpwd=vpwd
        
    def register(self):
        ur=UserRepository()
        self.registerValidate(self.user,self.pwd,self.vpwd)
        ur.create_user(self.user,self.pwd)

    def login(self):
        self.loginValidate()

    def registerValidate(self,user,pwd,vpwd):
        ur=UserRepository()
        if user == "" or pwd == "":
            raise ValueError("Ningun campo puede estar vacio")
        
        if len(user)<4:
            raise ValueError("Nombre de usuario demasiado corto")
        
        if len(pwd)<4:
            raise ValueError("Contrasenia demasiado corta")
        
        if pwd != vpwd:
            raise ValueError("Las contrasenias no coinciden")
        
        if ur.user_exists(user):
            raise ValueError("El usuario ya existe")

    def loginValidate(self):
        ur=UserRepository()
        if not ur.user_exists(self.user):
            raise ValueError("Usuario o contrasenia invalida")
        
        if not ur.user_valid(self.user,self.pwd):
            raise ValueError("Usuario o contrasenia invalida")