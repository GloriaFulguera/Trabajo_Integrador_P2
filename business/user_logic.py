from data.data_helper import data_helper
from os.path import exists
import bcrypt

class userLogic:

    def __init__(self,user,pwd,vpwd=None):
        self.user=user
        self.pwd=pwd
        self.vpwd=vpwd
        
    def register(self):
        dh=data_helper()

        data=dh.deserialize("data/usuarios.json")
        data[self.user] = bcrypt.hashpw(self.pwd.encode(), bcrypt.gensalt()).decode()

        dh.serialize(data,"data/usuarios.json")

    def validations(self,user,pwd,vpwd):
        if user == "" or pwd == "":
            raise ValueError("Ningun campo puede estar vacio")
        
        if pwd != vpwd:
            raise ValueError("Las contrasenias no coinciden")
        
        dh=data_helper()
        if not exists("data/usuarios.json"):
            dh.serialize({},"data/usuarios.json")

        usuarios=dh.deserialize("data/usuarios.json")
        if user in usuarios:
            raise ValueError("El usuario ya existe")

    def loginValidate(self):
        dh=data_helper()
        if not exists("data/usuarios.json"):
            dh.serialize({},"data/usuarios.json")
        
        usuarios=dh.deserialize("data/usuarios.json")
        
        if not self.user in usuarios:
            raise ValueError("Usuario o contrasenia invalida")
        
        if not bcrypt.checkpw(self.pwd.encode(),usuarios[self.user].encode()):
            raise ValueError("Usuario o contrasenia invalida")