import json

class Usuario:
    def __init__(self,user,pwd):
        self.user=user
        self.password=pwd

    def toDict(self):
        return {self.user:self.password}

    def fromDict(self,source):
        for key in source.keys():
            setattr(self,key,source[key])


class data_helper:
    def __init__(self):
        pass

    def serialize(self,obj,name):
        with open(name,"w") as f:
            f.write(json.dumps(obj,indent=4))

    def deserialize(self,name):
        with open(name,"r") as f:
            txt=f.read()
            return json.loads(txt)
        