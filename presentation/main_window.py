from PyQt6.QtWidgets import QMainWindow,QMessageBox
from PyQt6.QtCore import pyqtSignal
from presentation.screens.MainWindow_ui import Ui_MainWindow
from business.transaction_logic import transactionLogic
from decimal import Decimal,InvalidOperation
import time

class MainWindow(QMainWindow,Ui_MainWindow):
    logoutRequested=pyqtSignal()

    def __init__(self,user):
        super().__init__()
        self.setupUi(self)
        self.lblWelcomeUser.setText("Sesión de "+user)
        self.btnCerrar.clicked.connect(self.logout)
        self.logic=transactionLogic(user)

        self.btnCreateAccountM.clicked.connect(self.showCreateAccount)
        self.btnPurchaseM.clicked.connect(self.showPurchase)
        self.btnSellM.clicked.connect(self.showSell)
        self.btnDepositM.clicked.connect(self.showDeposit)

        self.btnCreateAccount_3.clicked.connect(self.create_account)
        self.btnPurchase.clicked.connect(self.purchase_currency)
        self.btnSell.clicked.connect(self.sell_currency)
        self.btnDeposit.clicked.connect(self.deposit_amount)

    def create_account(self):
        try:
            self.validateEmpty(self.cmbCurrency_3.currentText())
            self.logic.createAccount(self.cmbCurrency_3.currentText())

            QMessageBox.information(self,"Info","La cuenta fue generada satisfactoriamente.")
        except ValueError as error:
            QMessageBox.warning(self,"Advertencia",str(error))

    def purchase_currency(self):
        try:
            self.validateEmpty(self.txtPurchaseAmount.text())
            self.validateEmpty(self.cmbPurchaseCurrency.currentText())
            curr=self.cmbPurchaseCurrency.currentText()
            amount=Decimal(self.txtPurchaseAmount.text())
            ltsRates=self.logic.validateExchange("ARS",curr,amount,"compra")

            tinicio=time.time()
            rta = QMessageBox.information(self,"Confirmacón","¿Está seguro de que desea continuar con la operación?",buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if (time.time()-tinicio)>10:
                rta=QMessageBox.StandardButton.No
            if rta == QMessageBox.StandardButton.Yes:
                self.logic.completeExchange("ARS",curr,amount,self.logic.getTotalPurchase("ARS",curr,amount,ltsRates))
                QMessageBox.information(self,"Info","Operación realizada con éxito.")
            else:
                QMessageBox.warning(self,"Advertencia","La operación fue cancelada.")
            self.cleanInputs()

        except InvalidOperation:
            QMessageBox.warning(self,"Advertencia","El valor ingresado es inválido.")
        except ValueError as error:
            QMessageBox.warning(self,"Advertencia",str(error))

    def sell_currency(self):
        try:
            self.validateEmpty(self.txtSellAmount.text())
            self.validateEmpty(self.cmbSellCurrency.currentText())
            amount=Decimal(self.txtSellAmount.text())
            curr=self.cmbSellCurrency.currentText()
            ltsRates=self.logic.validateExchange(curr,"ARS",amount,"venta")

            tinicio=time.time()
            rta = QMessageBox.information(self,"Confirmacón","¿Está seguro de que desea continuar con la operación?",buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if (time.time()-tinicio)>10:
                rta=QMessageBox.StandardButton.No
            if rta == QMessageBox.StandardButton.Yes:
                self.logic.completeExchange(curr,"ARS",self.logic.getTotalSell(curr,"ARS",amount,ltsRates),amount)
                QMessageBox.information(self,"Info","Operación realizada con éxito.")
            else:
                QMessageBox.warning(self,"Advertencia","La operación fue cancelada.")
            self.cleanInputs()

        except InvalidOperation:
            QMessageBox.warning(self,"Advertencia","El valor ingresado es inválido.")
        except ValueError as error:
            QMessageBox.warning(self,"Advertencia",str(error))

    def deposit_amount(self):
        try:
            self.validateEmpty(self.txtAmount.text())
            amount=Decimal(self.txtAmount.text())
            self.logic.depositAmount(amount,"ARS")

            QMessageBox.information(self,"Info","Depósito exitoso.")
            self.cleanInputs()

        except InvalidOperation:
            QMessageBox.warning(self,"Advertencia","El valor ingresado es inválido.")
        except ValueError as error:
            QMessageBox.warning(self,"Advertencia",str(error))

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