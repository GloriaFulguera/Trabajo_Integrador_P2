from PyQt6.QtWidgets import QDialog,QMessageBox
from presentation.screens.AuthWindow_ui import Ui_AuthWindow
from business.user_logic import userLogic      

class AuthDialog(QDialog,Ui_AuthWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackAuth.setCurrentIndex(0)
        self.btnRegister.clicked.connect(self.showRegister)
        self.btnLoginR.clicked.connect(self.showLogin)
        self.btnLogin.clicked.connect(self.login)
        self.btnRegisterR.clicked.connect(self.registration)

    def showLogin(self):
        self.stackAuth.setCurrentIndex(0)
        self.cleanInputs()

    def showRegister(self):
        self.stackAuth.setCurrentIndex(1)
        self.cleanInputs()

    def login(self):
        try:
            self.validateEmpty(self.txtUsuario.text())
            self.validateEmpty(self.txtPassword.text())
            logica=userLogic(self.txtUsuario.text(),self.txtPassword.text())
            logica.login()
            self.accept()

        except ValueError as error:
            QMessageBox.warning(self,"Advertencia",str(error))

    def registration(self):
        try:
            self.validateEmpty(self.txtUserRegister.text())
            self.validateEmpty(self.txtPwdRegister.text())
            self.validateEmpty(self.txtPwdValidate.text())
            logica=userLogic(self.txtUserRegister.text(),self.txtPwdRegister.text(),self.txtPwdValidate.text())
            logica.register()
            QMessageBox.information(self,"Info","Usuario registrado correctamente")
            self.cleanInputs()

        except ValueError as error:
            QMessageBox.warning(self,"Advertencia",str(error))

    def validateEmpty(self,value):
        if str(value).strip() == "":
            raise ValueError("Debe completar todos los campos.")
        
    def cleanInputs(self):
        self.txtUsuario.clear()
        self.txtPassword.clear()
        self.txtUserRegister.clear()
        self.txtPwdRegister.clear()
        self.txtPwdValidate.clear()