import sys
from PyQt6.QtWidgets import QApplication
from presentation.auth_dialog import AuthDialog
from presentation.main_window import MainWindow

if __name__=="__main__":
    app=QApplication([])

    auth=AuthDialog()
    if auth.exec():
        win=MainWindow(auth.user)

        def logout_execute():
            dlg=AuthDialog()
            if dlg.exec():
                win.user=dlg.user
                win.lblWelcomeUser.setText("Sesión de "+dlg.user)
                win.show()

        win.logoutRequested.connect(logout_execute)

        win.show()
        sys.exit(app.exec())