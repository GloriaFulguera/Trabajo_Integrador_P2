from data.data_repository import UserRepository
from business.control_user import CheckEmpty,CheckUsername,CheckStrongPassword,CheckPassword,CheckUserExist,CheckUser,CheckUserRegistry

class userLogic:

    def __init__(self,user,pwd,vpwd=None):
        self.user=user
        self.pwd=pwd
        self.vpwd=vpwd
        
    def register(self):
        ur=UserRepository()
        self.registerValidate(self.user,self.pwd,self.vpwd)
        ur.create_user(self.user,self.pwd)

    def login(self):
        self.loginValidate(self.user,self.pwd)

    def registerValidate(self,user,pwd,vpwd):
        controls=CheckEmpty(user,pwd)
        controls.setNext(CheckUsername(user))\
        .setNext(CheckStrongPassword(pwd))\
        .setNext(CheckPassword(pwd,vpwd))\
        .setNext(CheckUserExist(user))

        controls.handle(user)

    def loginValidate(self,user,pwd):
        controls=CheckUser(user)
        controls.setNext(CheckUserRegistry(user,pwd))

        controls.handle(user)

        