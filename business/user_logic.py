from data.data_helper import data_helper,Usuario

class userLogic:

    def __init__(self,user,pwd):
        self.user=user
        self.pwd=pwd
        
    def registrar(self):
        us=Usuario(self.user,self.pwd)
        dh=data_helper()
        dh.serialize(us.toDict(),"usuario.json")