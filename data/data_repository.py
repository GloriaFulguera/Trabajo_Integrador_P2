from data.data_helper import data_helper
import bcrypt

class UserRepository:
    def __init__(self, archivo="data/usuarios.json"):
        self.archivo=archivo
        self.dh=data_helper()

    def create_user(self,user,pwd):
        usuarios=self.dh.deserialize(self.archivo)
        usuarios[user] = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()
        self.dh.serialize(usuarios,self.archivo)

    def user_exists(self,user):
        usuarios=self.dh.deserialize(self.archivo)
        if user in usuarios:
            return True
        else:
            return False

    def user_valid(self,user,pwd):
        usuarios=self.dh.deserialize(self.archivo)
        return bcrypt.checkpw(pwd.encode(),usuarios[user].encode())
