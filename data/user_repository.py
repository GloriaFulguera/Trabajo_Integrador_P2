import sqlobject as SO

database='mysql://guest:1234@localhost/prog2'
__connection__=SO.connectionForURI(database)

class User(SO.SQLObject):
    usuario=SO.StringCol(length=100, varchar=True)
    clave=SO.StringCol(length=200,varchar=True)

def createUser(p_user,p_pwd):
    user=None
    try:
        exist=User.selectBy(usuario=p_user)
        user=exist.getOne()
    except SO.SQLObjectNotFound:
        user= User(
            usuario=p_user,
            clave=p_pwd
        )
    return user