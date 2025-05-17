from data.data_helper import data_helper,Usuario
from os.path import exists

class userLogic:

    def __init__(self,user,pwd,vpwd=None):
        self.user=user
        self.pwd=pwd
        self.vpwd=vpwd
        
    def register(self):
        us=Usuario(self.user,self.pwd)
        dh=data_helper()

        data=dh.deserialize("usuarios.json")
        data[self.user]=self.pwd

        dh.serialize(data,"usuarios.json")

    def validations(self,user,pwd,vpwd):
        if pwd != vpwd:
            raise ValueError("Las contrasenias no coinciden")
        
        dh=data_helper()
        if not exists("usuarios.json"):
            dh.serialize({},"usuarios.json")

        usuarios=dh.deserialize("usuarios.json")
        print(usuarios)
        print(usuarios.keys())
        if user in usuarios:
            raise ValueError("El usuario ya existe")

    #TO DO: usar bcrypt para guardar la pass
    #TO DO: permitir registrar mas de un usuario? crear una lista de objetos
    #TO DO: modificar funcion login, luego del pendiente de arriba

    def login(self):
        us=Usuario(self.user,self.pwd)
        dh=data_helper()
        usuarios=dh.deserialize("usuarios.json")
        
        #us.prueba()

    def loginValidate(self):
        pass