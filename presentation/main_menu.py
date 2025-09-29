import sys
from PyQt6.QtWidgets import QApplication
from .auth_dialog import AuthDialog
from .main_window import MainWindow

class Menu:
    def showMenu(self):
        app = QApplication(sys.argv)

        auth = AuthDialog()
        if auth.exec():
            win = MainWindow(auth.user)

            def logout_execute():
                dlg = AuthDialog()
                if dlg.exec():
                    win.user = dlg.user
                    win.lblWelcomeUser.setText("Sesión de " + dlg.user)
                    win.show()

            win.logoutRequested.connect(logout_execute)
            win.show()
            sys.exit(app.exec())
