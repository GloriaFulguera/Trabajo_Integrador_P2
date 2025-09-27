import sys
from PyQt6.QtWidgets import QApplication
from presentation.auth_dialog import AuthDialog
from presentation.main_window import MainWindow

if __name__=="__main__":
    app=QApplication([])
    auth=AuthDialog()
    if auth.exec():
        win=MainWindow()
        win.show()
        sys.exit(app.exec())