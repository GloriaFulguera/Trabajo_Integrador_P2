from PyQt6.QtWidgets import QMainWindow
from presentation.screens.MainWindow import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)