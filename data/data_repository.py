import sqlobject as SO
from data.data_helper import data_helper
import bcrypt

database='mysql://guest:1234@localhost/prog2'
__connection__=SO.connectionForURI(database)

class Usuarios(SO.SQLObject):
    usuario=SO.StringCol(length=100, varchar=True)
    clave=SO.StringCol(length=200,varchar=True)
    cuentas=SO.MultipleJoin('Cuentas', joinColumn='id_usuario')

class UserRepository:
    #def __init__(self):
        #self.archivo=archivo
        #self.dh=data_helper()

    def create_user(self,p_user,p_pwd):
        #usuarios=self.dh.deserialize(self.archivo)
        hash=bcrypt.hashpw(p_pwd.encode(), bcrypt.gensalt()).decode()
        #usuarios[p_user] = hash
        #self.dh.serialize(usuarios,self.archivo)
        Usuarios(usuario=p_user, clave=hash)


    def user_exists(self,p_user):
        #usuarios2=self.dh.deserialize(self.archivo)
        try:
            existe=Usuarios.selectBy(usuario=p_user)
            existe.getOne()
            return True
        except SO.SQLObjectNotFound:
            return False

        # if p_user in usuarios2:
        #     return True
        # else:
        #     return False

    def user_valid(self,p_user,p_pwd):
        user=None
        try:
            existe=Usuarios.selectBy(usuario=p_user)
            user=existe.getOne()
            return bcrypt.checkpw(p_pwd.encode(), user.clave.encode())
        except SO.SQLObjectNotFound:
            return False
        # usuarios=self.dh.deserialize(self.archivo)
        # return bcrypt.checkpw(pwd.encode(),usuarios[user].encode())
