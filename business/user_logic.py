from data.data_helper import data_helper,Usuario

class userLogic:

    def __init__(self,user,pwd,vpwd):
        self.user=user
        self.pwd=pwd
        self.vpwd=vpwd
        
    def register(self):
        us=Usuario(self.user,self.pwd)
        dh=data_helper()
        dh.serialize(us.toDict(),"usuario.json")

    def passwordValidate(self,pwd,vpwd):
        if pwd != vpwd:
            raise ValueError("Las contrasenias no coinciden")