import json

class Usuario:
    def __init__(self,user,pwd):
        self.user=user
        self.password=pwd

    def toDict(self):
        ret={}
        for attr in dir(self):
            if not attr.startswith("__") and not attr.endswith("__"):
                val=getattr(self,attr)
                if not callable(val):
                    ret[attr]=val
        return ret

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