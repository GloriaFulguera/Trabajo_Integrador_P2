from PyQt6.QtWidgets import QDialog
from screens.AuthWindow_ui import Ui_AuthWindow

class AuthDialog(QDialog,Ui_AuthWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackAuth.setCurrentIndex(0)
        self.btnRegister.clicked.connect(self.showRegister)
        self.btnLoginR.clicked.connect(self.showLogin)

    def showLogin(self):
        self.stackAuth.setCurrentIndex(0)

    def showRegister(self):
        self.stackAuth.setCurrentIndex(1)