from data.data_helper import data_helper,Usuario

class userLogic:

    def __init__(self,user,pwd,vpwd=None):
        self.user=user
        self.pwd=pwd
        self.vpwd=vpwd
        
    def register(self):
        us=Usuario(self.user,self.pwd)
        dh=data_helper()
        dh.serialize(us.toDict(),"usuario.json")

    def validations(self,user,pwd,vpwd):
        if pwd != vpwd:
            raise ValueError("Las contrasenias no coinciden")
        
        dh=data_helper()
        usuarios=dh.deserialize("usuario.json")
        print(usuarios)
        print(usuarios.keys())
        if usuarios['user']==user:
            raise ValueError("El usuario ya existe")

    #TO DO: usar bcrypt para guardar la pass
    #TO DO: permitir registrar mas de un usuario? crear una lista de objetos
    #TO DO: re-configurar lista, para identificar el username como key?
    #TO DO: modificar funcion login, luego del pendiente de arriba

    def login(self):
        us=Usuario(self.user,self.pwd)
        dh=data_helper()
        usuarios=dh.deserialize("usuario.json")
        
        #us.prueba()

    def loginValidate(self):
        pass