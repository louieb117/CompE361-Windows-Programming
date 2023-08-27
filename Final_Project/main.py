from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import pandas as pd
import sys
from PyQt5.uic.properties import QtGui
from AdminMain import AdminMain
from UserMain import UserMain


class Login(QMainWindow):

    def __init__(self):
        # QMainWindow initialization
        super(Login, self).__init__()

        # Load UI file
        uic.loadUi('UI/UM.ui', self)
        self.show()

        # Excel file
        self.df_users = pd.read_excel('database_copy.xlsx', sheet_name='users')   # Data frame
        #self.user = self.df_users.loc[self.df_users.id == id].reset_index()


        #self.show_admin_store_page() # Show Admin Window
        #self.show_user_store_page()  # Show User Window


        # Button
        self.pb_login.clicked.connect(self.gui_state)

    def keyPressEvent(self, event: QKeyEvent) -> None:

        if event.key() == Qt.Key_Return:
            print('*** Enter pressed')
            self.gui_state()
        if event.key() == Qt.Key_Escape:
            print('*** Escape pressed')
            sys.exit(app.exec())

    def login_gate(self):
        # Load UI file
        uic.loadUi('UI/UM.ui', self)
        self.show()

        # Button
        self.pb_login.clicked.connect(self.gui_state)

    def gui_state(self):
        print(self.le_password.text())
        self.log_user = self.df_users.loc[self.df_users.username == self.le_username.text()].reset_index()
        try:
            self.log_password = str(int(self.log_user.loc[0].at['password']))
        except ValueError as ve:
            self.log_password = str(self.log_user.loc[0].at['password'])

        # Check if empty or not in db
        if len(self.log_user) != 0:
            # Check if the logged user is admin
            if self.log_user.admin.bool():
                # Check password
                if self.log_password == self.le_password.text():
                    self.show_admin_store_page()
                else:
                    self.invalid_password_window()
            # User
            else:
                if self.log_password == self.le_password.text():
                    self.show_user_store_page()
                else:
                    self.invalid_password_window()

        else:
            mb = QMessageBox()
            mb.setWindowTitle('Invalid Username')
            mb.setText('Invalid Username\nUsername not found')
            mb.setStandardButtons(QMessageBox.Ok)
            res = mb.exec()
            if res == QMessageBox.Ok:
                self.close()
                self.login_gate()

    def invalid_password_window(self):
        mb = QMessageBox()
        mb.setWindowTitle('Invalid password')
        mb.setText('Invalid password\nPlease try again')
        mb.setStandardButtons(QMessageBox.Ok)
        res = mb.exec()
        if res == QMessageBox.Ok:
            self.close()
            self.login_gate()

    def show_admin_store_page(self):
        self.show_admin_store_gui = AdminMain()
        self.close()

    def show_user_store_page(self):
        self.show_user_store_gui = UserMain.UserMain('UI/UserMain.ui')
        self.close()

if __name__ == '__main__':
    app = QApplication([])
    window = Login()
    sys.exit(app.exec())
