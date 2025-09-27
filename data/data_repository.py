import sqlobject as SO
from os import getenv
from dotenv import load_dotenv
import bcrypt

load_dotenv()
__connection__=SO.connectionForURI(getenv("DATABASE"))

class Usuarios(SO.SQLObject):
    usuario=SO.StringCol(length=100, varchar=True)
    clave=SO.StringCol(length=200,varchar=True)
    cuentas=SO.MultipleJoin('Cuentas', joinColumn='id_usuario')

class UserRepository:

    def create_user(self,p_user,p_pwd):
        hash=bcrypt.hashpw(p_pwd.encode(), bcrypt.gensalt()).decode()
        Usuarios(usuario=p_user, clave=hash)

    def user_exists(self,p_user):
        try:
            existe=Usuarios.selectBy(usuario=p_user)
            existe.getOne()
            return True
        except SO.SQLObjectNotFound:
            return False

    def user_valid(self,p_user,p_pwd):
        user=None
        try:
            existe=Usuarios.selectBy(usuario=p_user)
            user=existe.getOne()
            return bcrypt.checkpw(p_pwd.encode(), user.clave.encode())
        except SO.SQLObjectNotFound:
            return False

