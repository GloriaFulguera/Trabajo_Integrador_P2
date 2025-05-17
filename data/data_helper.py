import json

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
        