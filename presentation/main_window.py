from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSignal
from presentation.screens.MainWindow_ui import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    logoutRequested=pyqtSignal()

    def __init__(self,user):
        super().__init__()
        self.setupUi(self)
        self.lblWelcomeUser.setText("Sesión de "+user)
        self.btnCerrar.clicked.connect(self.logout)
        self.user=user
        self.btnCreateAccountM.clicked.connect(self.showCreateAccount)
        self.btnPurchaseM.clicked.connect(self.showPurchase)
        self.btnSellM.clicked.connect(self.showSell)
        self.btnDepositM.clicked.connect(self.showDeposit)


    def validateEmpty(self,value):
        if str(value).strip() == "":
            raise ValueError("Debe completar todos los campos.")
        
    def cleanInputs(self):
        self.txtAmount.clear()
        self.txtPurchaseAmount.clear()
        self.txtSellAmount.clear()

    def logout(self):
        self.hide()
        self.logoutRequested.emit()

    def showCreateAccount(self):
        self.stackMain.setCurrentIndex(0)

    def showPurchase(self):
        self.stackMain.setCurrentIndex(1)

    def showSell(self):
        self.stackMain.setCurrentIndex(2)

    def showDeposit(self):
        self.stackMain.setCurrentIndex(3)