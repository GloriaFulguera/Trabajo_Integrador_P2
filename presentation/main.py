import sys
from PyQt6.QtWidgets import QApplication
from auth_dialog import AuthDialog

if __name__=="__main__":
    app=QApplication([])
    auth=AuthDialog()
    auth.show()
    sys.exit(app.exec())