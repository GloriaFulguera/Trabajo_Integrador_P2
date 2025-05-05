from data.data_helper import data_helper,usuario

class userLogic:

    def __init__(self,user,password):
        self.user=user
        self.password=password
        
    def registrar(self):
        us=usuario(self.user,self.password)
        dh=data_helper()
        dh.serialize(us.toDict(),"usuario.json")